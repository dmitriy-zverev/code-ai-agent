import os
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part[0].name}({function_call_part[0].args})")
    else:
        print(f" - Calling function: {function_call_part[0].name}")
    
    function_result = None

    match function_call_part[0].name:
        case "get_file_content":
            function_result = get_file_content("./calculator", **function_call_part[0].args)
        case "get_files_info":
            function_result = get_files_info("./calculator", **function_call_part[0].args)
        case "run_python_file":
            function_result = run_python_file("./calculator", **function_call_part[0].args)
        case "write_file":
            function_result = write_file("./calculator", **function_call_part[0].args)
        case _:
            function_result = types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part[0].name,
                        response={"error": f"Unknown function: {function_call_part[0].name}"}
                    )
                ]
            )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part[0].name,
                response={"function_result": function_result}
            )
        ]
    )