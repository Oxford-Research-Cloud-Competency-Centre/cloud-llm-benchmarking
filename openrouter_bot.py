import os
import json
import requests
import re
from pathlib import Path
from collections import defaultdict

def get_available_models():
    """Get list of available models from OpenRouter."""
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "X-Title": "LLM Benchmarking"
    }
    
    try:
        response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
        response.raise_for_status()
        models = response.json()["data"]
        
        # Group models by owner
        grouped_models = defaultdict(dict)
        for model in models:
            owner = model["id"].split('/')[0]
            grouped_models[owner][model["id"]] = {
                "name": model["name"],
                "context_length": model.get("context_length", "Unknown")
            }
        
        # Sort owners alphabetically
        return dict(sorted(grouped_models.items()))
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'text'):
            error_detail = e.response.text
        else:
            error_detail = str(e)
        raise Exception(f"Error fetching models: {error_detail}")

def display_models(grouped_models, search_term=None):
    """Display models with optional search."""
    model_count = 1
    model_map = {}  # Maps display number to model ID
    
    # Filter models if search term is provided
    if search_term:
        search_term = search_term.lower()
        filtered_models = {}
        for owner, models in grouped_models.items():
            filtered_models[owner] = {
                model_id: info for model_id, info in models.items()
                if search_term in model_id.lower() or 
                   search_term in info['name'].lower()
            }
            if filtered_models[owner]:
                filtered_models[owner] = dict(sorted(filtered_models[owner].items()))
    else:
        filtered_models = grouped_models

    print("\nAvailable models:")
    
    for owner, models in filtered_models.items():
        if not models:
            continue
            
        print(f"\n{owner.upper()}:")
        for model_id, model_info in models.items():
            print(f"{model_count}. {model_info['name']} ({model_id})")
            model_map[model_count] = model_id
            model_count += 1
    
    return model_map

def get_prompt_files():
    """Get all .txt files from the PROMPTS directory."""
    prompts_dir = "PROMPTS"
    if not os.path.exists(prompts_dir):
        return []
    
    return [f for f in os.listdir(prompts_dir) if f.endswith('.txt')]

def read_prompt(prompt_filename):
    """Read a prompt file from the PROMPTS directory."""
    prompt_path = os.path.join("PROMPTS", prompt_filename)
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"prompt not found at {prompt_path}")
    
    with open(prompt_path, 'r') as f:
        return f.read()

def extract_code(text):
    """Extract Python code from the model's response."""
    # Look for code blocks marked with ```python or ```
    code_blocks = re.findall(r'```(?:python)?\n(.*?)```', text, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()
    
    # If no code blocks found, try to find any Python-like code
    # This is a fallback and might not be perfect
    lines = text.split('\n')
    code_lines = []
    in_code = False
    
    for line in lines:
        # Skip lines that look like markdown or comments
        if line.strip().startswith(('#', '```', '>', '*')):
            continue
        # Skip empty lines at the start
        if not code_lines and not line.strip():
            continue
        # Add the line if it looks like code
        if any(keyword in line for keyword in ['def ', 'class ', 'import ', 'from ', 'return ', 'if ', 'for ', 'while ']):
            in_code = True
        if in_code:
            code_lines.append(line)
    
    return '\n'.join(code_lines).strip()

def generate_output(api_key, model_id, prompt):
    """Generate output using OpenRouter API."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/pauld/llm-benchmarking", 
        "X-Title": "LLM Benchmarking" 
    }
    
    # Add system message to encourage code-only response
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "system",
                "content": "You are a Python programming expert. Provide only the Python code solution without any explanations or markdown formatting. The code should be complete and runnable."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 4096
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", 
                               headers=headers, 
                               json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'text'):
            error_detail = e.response.text
        else:
            error_detail = str(e)
        raise Exception(f"API Error for model {model_id}: {error_detail}")

def save_output(problem_folder, output, output_prefix):
    """Save the generated output to a file."""
    # Extract code from the response
    code = extract_code(output)
    
    # Save as .py file
    output_path = os.path.join(problem_folder, f"{output_prefix}.py")
    with open(output_path, 'w') as f:
        f.write(code)

def validate_model(api_key, model_id):
    """Validate if a model is actually available for use."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/pauld/llm-benchmarking",
        "X-Title": "LLM Benchmarking"
    }
    
    # Try a minimal request to validate the model
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": "test"
            }
        ],
        "max_tokens": 128
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", 
                               headers=headers, 
                               json=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'text'):
            error_detail = e.response.text
        else:
            error_detail = str(e)
        raise Exception(f"Model validation failed: {error_detail}")

def main():
    # Get API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        api_key = input("Please enter your OpenRouter API key: ").strip()
    
    # Get available models
    print("Fetching available models...")
    try:
        grouped_models = get_available_models()
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    # Display all models
    model_map = display_models(grouped_models)
    
    # Get model selection and validate
    selected_model = None
    while selected_model is None:
        try:
            model_choice = int(input("\nSelect a model number: "))
            if 1 <= model_choice <= len(model_map):
                selected_model = model_map[model_choice]
                print(f"\nValidating model {selected_model}...")
                try:
                    validate_model(api_key, selected_model)
                    print("Model is available!")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    print("Please select a different model number from the list above.")
                    selected_model = None
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Get output prefix
    output_prefix = input("\nEnter name for output files (e.g., 'claude', 'gpt4'): ").strip()
    if not output_prefix:
        output_prefix = "model"

    # Process prompt files
    prompt_files = get_prompt_files()
    print(f"\nFound {len(prompt_files)} prompt files")

    for prompt_file in prompt_files:
        # Extract problem name from filename (remove .txt extension)
        problem_name = prompt_file[:-4]  # Remove .txt extension
        output_folder = problem_name
        output_path = os.path.join(output_folder, f"{output_prefix}.py")
        
        if os.path.exists(output_path):
            print(f"\nSkipping {problem_name} - output file already exists: {output_path}")
            continue
        
        print(f"\nProcessing {problem_name}...")
        try:
            prompt = read_prompt(prompt_file)
            print("Generating output...")
            output = generate_output(api_key, selected_model, prompt)
            save_output(output_folder, output, output_prefix)
            print(f"Output saved to {output_folder}/{output_prefix}.py")
        except Exception as e:
            print(f"Error processing {problem_name}: {str(e)}")

if __name__ == "__main__":
    main() 