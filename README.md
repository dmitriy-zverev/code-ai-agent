# CodeWhisperer 🤖

An autonomous AI coding assistant that understands your problems and fixes your code without you lifting a finger.

## Description

CodeWhisperer is an intelligent CLI tool that acts as your personal coding companion. Simply describe what's wrong with your code in plain English (even with emojis!), and watch as it autonomously navigates your project, identifies issues, and implements fixes. Think of it as having a senior developer who never sleeps, never gets tired, and always knows exactly what to do.

## Why? 🤔

**The Problem:** Debugging and fixing code can be time-consuming and frustrating. You know something's broken, but finding the root cause and implementing the right fix often involves:
- Manually scanning through multiple files
- Understanding complex codebases
- Writing and testing fixes
- Repeating the process until everything works

**The Solution:** CodeWhisperer eliminates this tedious cycle by:
- **Understanding natural language**: Describe your problem however you want
- **Autonomous exploration**: Intelligently scans your project structure
- **Smart debugging**: Identifies root causes across multiple files
- **Automatic fixes**: Implements and tests solutions
- **Iterative improvement**: Keeps working until the problem is solved

**Real Impact:** Turn hours of debugging into minutes of waiting. Focus on building features instead of hunting bugs.

## Quick Start

### Prerequisites
- Python 3.13+ installed
- [uv](https://docs.astral.sh/uv/) package manager
- Google Gemini API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dmitriy-zverev/code-ai-agent.git
   cd code-ai-agent
   ```

2. **Set up your environment:**
   ```bash
   # Create .env file with your API key
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   ```

4. **Run your first fix:**
   ```bash
   uv run main.py "fix my calculator app, it's not starting correctly"
   ```

## Usage

### Basic Command Structure
```bash
uv run main.py "<describe your problem in plain English>"
```

### Real Examples

**Fix a broken application:**
```bash
uv run main.py "my calculator app crashes when I try to run it"
```

**Debug specific functionality:**
```bash
uv run main.py "strings aren't splitting correctly in my app, please fix 🥺👉🏽👈🏽"
```

**Verbose output for debugging:**
```bash
uv run main.py "fix the import errors" --verbose
```

### What CodeWhisperer Can Do

- **File Analysis**: Automatically scans your project structure
- **Code Reading**: Examines file contents to understand context
- **Smart Editing**: Modifies files with precise fixes
- **Testing**: Runs Python scripts to verify fixes work
- **Iterative Problem Solving**: Continues until the issue is resolved

### Example Output
```
> uv run main.py "fix my calculator app, its not starting correctly"

# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file

Code AI Agent: Great! The calculator app now seems to be working correctly. 
The output shows the expression and the result in a formatted way.
```

## Prerequisites
* Python 3.10+ installed
* uv project and package manager
* Be really cautious running this program