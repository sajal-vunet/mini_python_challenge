import sys
import subprocess

WELCOME_MESSAGE = """
Welcome to the Python File/Directory Search Utility!

Usage:
    python -m Python_Challenge [search_term] [options]

Options:
    --only-file      Only look for files.
    --only-dir       Only look for directories.
    --ext EXT        Only return results with this extension (e.g., py for Python files).
    --only-name      Only display names of the files/directories.

Examples:
    python -m Python_Challenge test
    python -m Python_Challenge data --only-dir
    python -m Python_Challenge script --only-file --ext py
"""

def main():
    print(WELCOME_MESSAGE)
    if len(sys.argv) < 2:
        print("Please provide a search term and any desired options.")
        sys.exit(1)
    # Forward all arguments to mini_challenge.py
    subprocess.run([sys.executable, "mini_challenge.py"] + sys.argv[1:])

if __name__ == "__main__":
    main()
