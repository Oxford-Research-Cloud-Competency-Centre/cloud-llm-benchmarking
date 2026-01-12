#!/usr/bin/env python3
"""
Script to identify which solution files are not runnable Python scripts.
Checks for syntax errors and basic execution errors.
"""
import os
import sys
import subprocess
import py_compile
from collections import defaultdict

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

def check_syntax(filepath):
    """Check if a Python file has valid syntax."""
    try:
        py_compile.compile(filepath, doraise=True)
        return True, None
    except py_compile.PyCompileError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def check_execution(filepath, timeout=2):
    """Check if a Python file can execute (even if it fails at runtime)."""
    try:
        # Try to run the script with empty input
        result = subprocess.run(
            [sys.executable, filepath],
            input="",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            text=True
        )
        # If it runs without syntax error, it's executable
        # We don't care about the return code or output
        return True, None
    except subprocess.TimeoutExpired:
        return False, "Timeout (script may be hanging)"
    except SyntaxError as e:
        return False, f"Syntax error: {str(e)}"
    except Exception as e:
        # If it's a runtime error (not syntax), the script is still "runnable"
        # Syntax errors would have been caught by check_syntax
        return True, None

def check_file(filepath):
    """Check a single Python file for syntax and execution issues."""
    results = {
        'syntax_ok': False,
        'execution_ok': False,
        'syntax_error': None,
        'execution_error': None
    }
    
    # Check syntax
    syntax_ok, syntax_error = check_syntax(filepath)
    results['syntax_ok'] = syntax_ok
    results['syntax_error'] = syntax_error
    
    # Only check execution if syntax is OK
    if syntax_ok:
        exec_ok, exec_error = check_execution(filepath)
        results['execution_ok'] = exec_ok
        results['execution_error'] = exec_error
    else:
        results['execution_ok'] = False
        results['execution_error'] = "Cannot execute due to syntax error"
    
    return results

def main():
    """Main function to check all solution files."""
    # Get the script's directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)
    
    print("=" * 70)
    print("Checking Python Solution Files for Syntax and Execution Errors")
    print("=" * 70)
    print()
    
    # Find all benchmark directories
    benchmark_dirs = find_benchmark_dirs()
    if not benchmark_dirs:
        print("No benchmark directories found!")
        return
    
    print(f"Found {len(benchmark_dirs)} problem directories\n")
    
    # Store results
    all_issues = defaultdict(list)
    total_files = 0
    syntax_errors = 0
    execution_errors = 0
    
    # Check each problem directory
    for problem_dir in sorted(benchmark_dirs):
        problem_path = os.path.join(root_dir, problem_dir)
        if not os.path.isdir(problem_path):
            continue
        
        print(f"Checking {problem_dir}/...")
        
        # Find all Python files in the directory
        python_files = [f for f in os.listdir(problem_path) if f.endswith('.py')]
        
        if not python_files:
            print(f"  No Python files found\n")
            continue
        
        problem_issues = []
        
        for filename in sorted(python_files):
            total_files += 1
            filepath = os.path.join(problem_path, filename)
            
            results = check_file(filepath)
            
            if not results['syntax_ok']:
                syntax_errors += 1
                issue = {
                    'problem': problem_dir,
                    'file': filename,
                    'type': 'syntax',
                    'error': results['syntax_error']
                }
                problem_issues.append(issue)
                all_issues[problem_dir].append(issue)
                print(f"  ❌ {filename}: Syntax error")
            elif not results['execution_ok']:
                execution_errors += 1
                issue = {
                    'problem': problem_dir,
                    'file': filename,
                    'type': 'execution',
                    'error': results['execution_error']
                }
                problem_issues.append(issue)
                all_issues[problem_dir].append(issue)
                print(f"  ⚠️  {filename}: Execution error")
            else:
                print(f"  ✓  {filename}: OK")
        
        if not problem_issues:
            print(f"  All files OK\n")
        else:
            print(f"  Found {len(problem_issues)} issue(s)\n")
    
    # Print summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files checked: {total_files}")
    print(f"Files with syntax errors: {syntax_errors}")
    print(f"Files with execution errors: {execution_errors}")
    print(f"Total non-runnable files: {syntax_errors + execution_errors}")
    print()
    
    # Print detailed report
    if all_issues:
        print("=" * 70)
        print("DETAILED REPORT")
        print("=" * 70)
        print()
        
        for problem_dir in sorted(all_issues.keys()):
            print(f"\n{problem_dir}/")
            print("-" * 70)
            
            for issue in all_issues[problem_dir]:
                print(f"  File: {issue['file']}")
                print(f"  Type: {issue['type'].upper()} ERROR")
                print(f"  Error: {issue['error']}")
                print()
        
        # Print list of all non-runnable files
        print("=" * 70)
        print("LIST OF NON-RUNNABLE FILES")
        print("=" * 70)
        for problem_dir in sorted(all_issues.keys()):
            for issue in all_issues[problem_dir]:
                print(f"{problem_dir}/{issue['file']}")
    else:
        print("✓ All files are runnable!")
    
    print()

if __name__ == "__main__":
    main()
