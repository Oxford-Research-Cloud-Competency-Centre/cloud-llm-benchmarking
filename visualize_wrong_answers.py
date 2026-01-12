#!/usr/bin/env python3
"""
Script to visualize wrong answers for a specific model and problem.
Usage: python visualize_wrong_answers.py <problem_name> <model_name>
Example: python visualize_wrong_answers.py reduced_row_echelon gpt5_1
"""

import sys
import os
import subprocess
import json
import re
from pathlib import Path

def run_evaluation_with_details(problem_dir, eval_script_path, model_file):
    """Run evaluation script and capture detailed results by executing it directly."""
    original_dir = os.getcwd()
    
    # Read the evaluation script before changing directory
    abs_eval_script = os.path.abspath(eval_script_path)
    with open(abs_eval_script, 'r') as f:
        eval_code = f.read()
    
    try:
        os.chdir(problem_dir)
        
        # Create a namespace with necessary imports and modules
        namespace = {
            '__name__': '__main__',
            '__file__': str(eval_script_path),
            'sys': sys,
            'os': os,
            'subprocess': subprocess,
            'time': __import__('time'),
            'random': __import__('random'),
            'numpy': __import__('numpy'),
        }
        
        # Try to import typing if needed
        try:
            namespace['typing'] = __import__('typing')
        except:
            pass
        
        # Suppress print output during evaluation
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        # Capture stdout to suppress evaluation output
        f = io.StringIO()
        with redirect_stdout(f), redirect_stderr(f):
            # Execute the code
            exec(compile(eval_code, abs_eval_script, 'exec'), namespace)
        
        # Extract results
        detailed_results = namespace.get('detailed_results', {})
        results = namespace.get('results', {})
        test_cases = namespace.get('test_cases', [])
        
        return detailed_results, results, test_cases
    finally:
        os.chdir(original_dir)

def format_matrix_input(input_str):
    """Format matrix input for better display."""
    lines = input_str.strip().split('\n')
    if not lines:
        return input_str
    
    # First line is dimensions
    dims = lines[0].split()
    if len(dims) == 2:
        n, m = dims
        matrix_lines = lines[1:]
        
        formatted = f"  Dimensions: {n} equations × {m} variables\n"
        formatted += "  Matrix (coefficients | constant):\n"
        for line in matrix_lines:
            # Format as a visual matrix
            values = line.split()
            if len(values) > 1:
                coeffs = values[:-1]
                const = values[-1]
                formatted += f"    [{' '.join(coeffs)} | {const}]\n"
            else:
                formatted += f"    {line}\n"
        return formatted.rstrip()
    
    return input_str

def visualize_wrong_answers(problem_name, model_name):
    """Visualize wrong answers for a specific model and problem."""
    problem_dir = Path(problem_name)
    eval_script = Path('EVALUATION') / f'{problem_name}.py'
    
    if not problem_dir.exists():
        print(f"Error: Problem directory '{problem_dir}' not found")
        return
    
    if not eval_script.exists():
        print(f"Error: Evaluation script '{eval_script}' not found")
        return
    
    model_file = f"{model_name}.py"
    model_path = problem_dir / model_file
    
    if not model_path.exists():
        print(f"Error: Model file '{model_path}' not found")
        return
    
    print(f"\n{'='*80}")
    print(f"Wrong Answers Visualization")
    print(f"Problem: {problem_name}")
    print(f"Model: {model_name}")
    print(f"{'='*80}\n")
    
    # Run evaluation to get detailed results
    print("Running evaluation...", end=' ', flush=True)
    detailed_results, results, test_cases = run_evaluation_with_details(str(problem_dir), str(eval_script), model_file)
    print("✓ Done\n")
    
    # Get wrong answers for this model
    failed_cases = detailed_results.get(model_file, [])
    
    if not failed_cases:
        score = results.get(model_file, {}).get('score', 'N/A')
        print(f"✓ No wrong answers found!")
        print(f"Score: {score}")
        return
    
    score = results.get(model_file, {}).get('score', 'N/A')
    print(f"Score: {score}")
    print(f"Number of wrong answers: {len(failed_cases)}\n")
    
    # Display each wrong answer
    for i, failure in enumerate(failed_cases, 1):
        print(f"{'─'*80}")
        print(f"Wrong Answer #{i}")
        print(f"{'─'*80}")
        print(f"Test Case #{failure['case_num']}: {failure.get('description', 'N/A')}")
        print()
        print("Input:")
        print(format_matrix_input(failure['input']))
        print()
        print(f"Expected Output: {failure['expected']}")
        if failure['actual']:
            print(f"Actual Output:   {failure['actual']}")
        else:
            print(f"Actual Output:   (empty/no output)")
        
        if 'error' in failure:
            print(f"\n❌ Error:")
            print(f"   {failure['error']}")
        
        if failure.get('stderr'):
            print(f"\n⚠️  Stderr:")
            # Indent stderr output
            for line in failure['stderr'].split('\n'):
                print(f"   {line}")
        
        print()
    
    print(f"{'='*80}")
    print(f"Summary: {len(failed_cases)} wrong answer(s) out of {len(test_cases)} test case(s)")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python visualize_wrong_answers.py <problem_name> <model_name>")
        print("Example: python visualize_wrong_answers.py reduced_row_echelon gpt5_1")
        sys.exit(1)
    
    problem_name = sys.argv[1]
    model_name = sys.argv[2]
    
    visualize_wrong_answers(problem_name, model_name)
