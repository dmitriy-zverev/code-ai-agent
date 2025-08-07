import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    full_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not full_path.startswith(full_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_info = os.listdir(full_path)
        dir_info = "\n".join(list(map(
            lambda item: f"- {item}: file_size={os.path.getsize(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}",
            dir_info
        )))
    except Exception as e:
        return f'Error listing files: {str(e)}'
    
    return dir_info

