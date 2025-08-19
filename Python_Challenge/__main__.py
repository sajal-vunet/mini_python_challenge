import sys
import subprocess
import shlex
import os

# This is the welcome message displayed when the package is run. It provides usage instructions.
WELCOME_MESSAGE = """
Welcome to the Python Search Utility!

Usage:
    python3 -m Python_Challenge --> this will display the welcome message and prompt for input

    [search_term] [options] --> actual search command to be executed

Options:
    --only-file      Only look for files.
    --only-dir       Only look for directories. 
    --ext            Only return files with this extension (e.g. py for Python files).
    --only-name      Only display names of the files/directories. Displays full paths by default.
    --root           Search from the root directory. Searches from the current directory by default.
"""

def main():
    print(WELCOME_MESSAGE)
    
    # Prompt the user for input
    user_input = input("\nEnter your search command:\n> ")

    # Check if the user input is empty
    if not user_input.strip():
        print("Error: No input provided. \n\nExiting...")
        sys.exit(1)

    pkg_dir = os.path.dirname(os.path.abspath(__file__))

    # Flow of control to mini_challenge.py
    mini_challenge_path = os.path.join(pkg_dir, "mini_challenge.py")
    if not os.path.exists(mini_challenge_path):
        print(f"Error: The file {mini_challenge_path} does not exist.")
        sys.exit(1)
    
    # Split the user input into arguments and run the mini_challenge.py script
    args = shlex.split(user_input)
    subprocess.run([sys.executable, mini_challenge_path] + args)

if __name__ == "__main__":
    main()
