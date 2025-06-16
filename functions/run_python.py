import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python", target_file], timeout=30, capture_output=True, text=True, check=True, cwd=abs_working_dir)
        if result:
            return_result = f"Ran {file_path}\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
            if result.returncode != 0:
                return_result += f"\nProcess exited with code {result.returncode}"
        else:
            return "No output produced."
        return return_result
    except Exception as e:
        return f"Error: executing Python file: {e}"
