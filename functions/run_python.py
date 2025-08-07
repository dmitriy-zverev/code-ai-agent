import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python script.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        command = ['python3', abs_file_path] + args

        completed_process = subprocess.run(
            command, 
            timeout=30,
            cwd=abs_working_dir,
            capture_output=True,
            text=True 
        )
        
        try: 
            final_output = f"STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}"
            if completed_process.returncode != 0:
                final_output += f"\nProcess exited with code {completed_process.returncode}"
            if not completed_process.stdout:
                final_output += "\nNo output produced."
        except Exception as e:
            return f"Error: executing Python file: {e}"
        return final_output
        
    except Exception as e:
        return f'Error: Cannot run file: {str(e)}'