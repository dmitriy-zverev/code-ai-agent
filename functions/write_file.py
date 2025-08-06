import os

def write_file(working_directory, file_path, content):
    full_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not full_path.startswith(full_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(os.path.abspath(full_path)):
        try:
            with open(full_path, 'x') as file:
                file.write(content)
        except Exception as e:
            return f'Error: Cannot write to file: {str(e)}'
    else:
        try:
            with open(full_path, 'w') as file:
                file.write(content)
        except Exception as e:
            return f'Error: File already exists or cannot be created: {str(e)}' 
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'