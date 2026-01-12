#!/usr/bin/env python3
"""
Script to automatically run benchmarks and regenerate code for models with wrong answers.
For each model in GENERAL_LLM_OPENROUTER_CODE:
- Skip if code is 0 (no longer available)
- Run benchmark
- For each problem with at least one wrong answer, regenerate the code
"""

import os
import sys
import subprocess
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Import from existing modules
from assistant_mapping import GENERAL_LLM_OPENROUTER_CODE
from openrouter_bot import (
    get_available_models, generate_output, extract_code, 
    read_prompt, get_prompt_files, save_output, display_models
)


def get_model_id(model_id_or_empty, grouped_models):
    """
    Get model ID from GENERAL_LLM_OPENROUTER_CODE.
    If model_id_or_empty is an empty string, return None (no longer available).
    If model_id_or_empty is a non-empty string, use it directly as the model ID.
    If model_id_or_empty is a number (old format), look it up in the model map.
    If model_id_or_empty is 0 (old format), return None.
    Returns the model ID if found, None otherwise.
    """
    # If it's an empty string or 0, model is no longer available
    if not model_id_or_empty or model_id_or_empty == 0:
        return None
    
    # If it's a non-empty string, it's the model ID (new format)
    if isinstance(model_id_or_empty, str):
        return model_id_or_empty
    
    # If it's a number (old format), look it up in the model map
    if isinstance(model_id_or_empty, int):
        model_map = display_models(grouped_models, search_term=None)
        return model_map.get(model_id_or_empty)
    
    return None


def parse_benchmark_output(output):
    """Parse the benchmark output to extract scores for each solution."""
    results = {}
    
    # Split output into lines
    lines = output.split('\n')
    
    # Look for lines with score patterns
    for line in lines:
        # Match pattern like "script.py    5/7     123.45"
        match = re.match(r'(\w+\.py)\s+(\d+)/(\d+)\s+', line)
        if match:
            script_name = match.group(1)
            correct = int(match.group(2))
            total = int(match.group(3))
            
            results[script_name] = {
                'correct': correct,
                'total': total,
                'has_wrong_answers': correct < total
            }
    
    return results


def run_benchmark_for_problem(problem_dir):
    """Run benchmark for a specific problem directory."""
    original_dir = os.getcwd()
    try:
        os.chdir(problem_dir)
        # Run the evaluation script from EVALUATION directory
        eval_script = os.path.join('..', 'EVALUATION', f'{problem_dir}.py')
        result = subprocess.run(
            [sys.executable, eval_script, '--no-details'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running benchmark in {problem_dir}: {e}")
        if e.stdout:
            print("Output:", e.stdout)
        if e.stderr:
            print("Error:", e.stderr)
        return None
    finally:
        os.chdir(original_dir)


def find_benchmark_dirs():
    """Find all directories that correspond to evaluation scripts in EVALUATION/."""
    eval_dir = 'EVALUATION'
    if not os.path.exists(eval_dir):
        return []
    
    # Get all problem directories that have corresponding evaluation scripts
    problem_dirs = []
    for eval_file in os.listdir(eval_dir):
        if eval_file.endswith('.py'):
            problem_name = eval_file[:-3]  # Remove .py extension
            problem_dir = os.path.join('.', problem_name)
            if os.path.isdir(problem_dir):
                problem_dirs.append(problem_name)
    
    return problem_dirs


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Run benchmarks and regenerate code for models with wrong answers'
    )
    parser.add_argument(
        '--model', '-m',
        action='append',
        help='Process only specific model(s). Can be used multiple times. Example: --model phi4 --model gpt4'
    )
    args = parser.parse_args()
    
    # Filter models if specified
    models_to_process = GENERAL_LLM_OPENROUTER_CODE
    if args.model:
        models_to_process = {}
        for model_name in args.model:
            if model_name in GENERAL_LLM_OPENROUTER_CODE:
                models_to_process[model_name] = GENERAL_LLM_OPENROUTER_CODE[model_name]
            else:
                print(f"Warning: Model '{model_name}' not found in GENERAL_LLM_OPENROUTER_CODE")
                print(f"Available models: {', '.join(sorted(GENERAL_LLM_OPENROUTER_CODE.keys()))}")
                sys.exit(1)
        print(f"Processing {len(models_to_process)} specified model(s): {', '.join(models_to_process.keys())}")
    
    # Get API key once
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        api_key = input("Please enter your OpenRouter API key: ").strip()
    
    # Set environment variable for subsequent calls (must be set before get_available_models)
    os.environ['OPENROUTER_API_KEY'] = api_key
    
    # Get available models
    print("Fetching available models from OpenRouter...")
    try:
        grouped_models = get_available_models()
    except Exception as e:
        print(f"Error fetching models: {str(e)}")
        return
    
    # Get all benchmark directories
    benchmark_dirs = find_benchmark_dirs()
    print(f"\nFound {len(benchmark_dirs)} benchmark directories: {', '.join(benchmark_dirs)}")
    
    # Run benchmarks ONCE for all problems (much faster than running for each model)
    print(f"\n{'='*60}")
    print("Running benchmarks for all problems (once)...")
    print(f"{'='*60}")
    all_problem_results = {}
    
    for problem_dir in benchmark_dirs:
        print(f"\nRunning benchmark for {problem_dir}...")
        output = run_benchmark_for_problem(problem_dir)
        if output:
            results = parse_benchmark_output(output)
            all_problem_results[problem_dir] = results
            print(f"  ✓ Completed - found {len(results)} solutions")
        else:
            print(f"  ✗ Failed to run benchmark")
    
    print(f"\n{'='*60}")
    print("Benchmark results collected. Processing models...")
    print(f"{'='*60}")
    
    # Process each model in the filtered list
    for technical_name, model_id_or_empty in models_to_process.items():
        # Skip if model_id is empty string or 0 (no longer available)
        if not model_id_or_empty or model_id_or_empty == 0:
            print(f"\n{'='*60}")
            print(f"Skipping {technical_name} (no longer available)")
            print(f"{'='*60}")
            continue
        
        print(f"\n{'='*60}")
        print(f"Processing model: {technical_name}")
        print(f"{'='*60}")
        
        # Get the model ID (handles both old number format and new string format)
        model_id = get_model_id(model_id_or_empty, grouped_models)
        if not model_id:
            print(f"Warning: Could not resolve model ID for {technical_name} (value: {model_id_or_empty}). Skipping.")
            continue
        
        print(f"Model ID: {model_id}")
        
        # Check which problems have wrong answers or missing files for this model
        model_file = f"{technical_name}.py"
        problems_to_regenerate = []
        
        print("\nChecking benchmark results and file existence...")
        for problem_dir in benchmark_dirs:
            file_path = os.path.join(problem_dir, model_file)
            file_exists = os.path.exists(file_path)
            
            if problem_dir in all_problem_results:
                results = all_problem_results[problem_dir]
                if model_file in results:
                    result = results[model_file]
                    print(f"  {problem_dir}/{model_file}: {result['correct']}/{result['total']}")
                    if result['has_wrong_answers']:
                        print(f"    ⚠️  Has wrong answers - will regenerate")
                        problems_to_regenerate.append(problem_dir)
                else:
                    if file_exists:
                        print(f"  {problem_dir}/{model_file}: File exists but not in benchmark results (may have failed)")
                        problems_to_regenerate.append(problem_dir)
                    else:
                        print(f"  {problem_dir}/{model_file}: File missing - will generate")
                        problems_to_regenerate.append(problem_dir)
            else:
                if file_exists:
                    print(f"  {problem_dir}/{model_file}: File exists but no benchmark results available")
                    # Don't regenerate if we don't have benchmark results - might be a benchmark issue
                else:
                    print(f"  {problem_dir}/{model_file}: File missing - will generate")
                    problems_to_regenerate.append(problem_dir)
        
        # Regenerate code for problems with wrong answers or missing files
        if problems_to_regenerate:
            print(f"\nRegenerating code for {len(problems_to_regenerate)} problem(s) with wrong answers...")
            prompt_files = get_prompt_files()
            
            for problem_dir in problems_to_regenerate:
                problem_name = problem_dir
                prompt_file = f"{problem_name}.txt"
                
                if prompt_file in prompt_files:
                    print(f"\n  Regenerating {problem_dir}/{model_file}...")
                    try:
                        prompt = read_prompt(prompt_file)
                        print(f"    Generating output with {model_id}...")
                        output = generate_output(api_key, model_id, prompt)
                        save_output(problem_dir, output, technical_name)
                        print(f"    ✓ Code regenerated and saved")
                    except Exception as e:
                        print(f"    ✗ Error regenerating code: {str(e)}")
                else:
                    print(f"  Warning: Prompt file {prompt_file} not found for {problem_dir}")
        else:
            print(f"\n  All answers correct for {technical_name}, no regeneration needed")
        
        print(f"\nCompleted processing {technical_name}")
    
    print(f"\n{'='*60}")
    print("All models processed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
