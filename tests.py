from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test_get_files_info():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))
    print()

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print()

    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print()

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
    print()

def test_get_file_content():
    print("Result for 'main.py':")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Result for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Result for '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Result for 'pkg/does_not_exist.txt':")
    print(get_file_content("calculator", "pkg/does_not_exist.txt"))
    print()

def test_write_file():
    print("Writing to 'lorem.txt':")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()

    print("Writing to 'pkg/morelorem.txt':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()

    print("Attempting to write outside working directory:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print()

def test_run_python_file():
    print("Running 'main.py' in 'calculator' directory:")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Running 'main.py' in 'calculator' directory with arguments ['3 + 5']:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("Running 'tests.py' in 'calculator' directory:")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("Running '../main.py' in 'calculator' directory:")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("Running 'nonexistent.py' in 'calculator' directory:")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

if __name__ == "__main__":
    test_run_python_file()