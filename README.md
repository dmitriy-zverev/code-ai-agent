# code-ai-agent
Code AI Agent is a toy version of Claude Code

## What is it
The program  is a CLI tool that:

1. Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽")
2. Chooses from a set of predefined functions to work on the task, for example:
* Scan the files in a directory
* Read a file's contents
* Overwrite a file's contents
* Execute the python interpreter on a file
3. Repeats step 2 until the task is complete (or it fails miserably, which is possible)

For example, I have a buggy calculator app, so I used my agent to fix the code:
```
> uv run main.py "fix my calculator app, its not starting correctly"
```
Output:
```
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Prerequisites
* Python 3.10+ installed
* uv project and package manager