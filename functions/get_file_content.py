import os
from config import MAX_FILE_CHARACTERS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory. If not provided, it will read the file in the working directory itself.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    full_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not full_path.startswith(full_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path, 'r') as file:
            content = file.read()
            if len(content) > MAX_FILE_CHARACTERS:
                content = content[:MAX_FILE_CHARACTERS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: Cannot read file: {str(e)}'
    
    return content