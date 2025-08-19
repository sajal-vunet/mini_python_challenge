import sys
import subprocess

WELCOME_MESSAGE = """
Welcome to the Python File/Directory Search Utility!

Usage:
    python3 -m Python_Challenge [search_term] [options]

Options:
    --only-file      Only look for files.
    --only-dir       Only look for directories.
    --ext EXT        Only return results with this extension (e.g., py for Python files).
    --only-name      Only display names of the files/directories.

Examples:
    python3 -m Python_Challenge test
    python3 -m Python_Challenge data --only-dir
    python3 -m Python_Challenge script --only-file --ext py
"""

def main():
    print(WELCOME_MESSAGE)
    # Prompt the user for input
    user_input = input("\nEnter your search command (e.g. test --only-file --ext py):\n> ")
    if not user_input.strip():
        print("No input provided. Exiting.")
        sys.exit(1)
    import shlex
    import os
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    mini_challenge_path = os.path.join(pkg_dir, "mini_challenge.py")
    args = shlex.split(user_input)
    subprocess.run([sys.executable, mini_challenge_path] + args)

if __name__ == "__main__":
    main()
