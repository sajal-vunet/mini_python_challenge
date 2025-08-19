# mini_python_challenge by Sajal Saxena
This repo contains the submission for Mini Python Challenge.

## Python_Challenge
This folder contains 2 files:
1. _ _main_ _.py
2. mini_challenge.py

### main.py
This file acts as the entry point for the program. It displays a welcome message along with the instructions for using the search functionality. It contains information about all the arguments. If the user enters an empty string as the input for search, the program is terminated by main.py itself. If the input is valid, the control is shifted to `mini_chalenge.py`.

### mini_challenge.py
This is where the program is actually run. It contains two functions:
1. searching(): This is used for performing the search. This function accepts 6 arguments:
  a. pattern: The search_term to be used for searching the files or directories.
  b. matches: An empty list used for storing paths of all the search results.
  c. only_file: A boolean flag which stores stores True if --only-files has been set in the CLI.
  d. only_dir: A boolean flag which stores True if --only-dir has been set in the CLI.
  e. ext: This stores the extension provided using --ext argument, if set in the CLI, otherwise NULL.
  f. root: This stores whether the root directory has to be used while searching, /home otherwise.

2. main: This is where the program is run. It parses the arguments using argparse library and stores the search_term. The searching() method is called here. It also uses time library to calculate the time taken during the execution of searching() function. It then displays the results of the search operation.

## Arguments
search_term: This is the string which has to be partially/fully matched with the name of the file or directory as mentioned by the user. This string has to be of minimum two characters in length, otherwise there will be an error. This is because a single character can lead to multiple unnecessary matches. The search implemented here is case-sensitive.

Optional Arguments available to the user:
- --only-file: This will only display the files having matching name as the search_term.
- --only-dir: This will only display the directories having matching name as the search_term.
- --only-name: This will only display the name of the file or directory. Not using this argument will result in the entire path of the file or directory being displayed.
- --ext: The user can specify the extension of the file they are searching for. Note that this argument cannot be used along with --only-dir because directories cannot have extensions.
- --root: This will start the search fromthe root directory. Not using this argument will set the search space to /home.

The results are printed to the stdout.

## Important Libraries Used
- pathlib: This library provides rglob() method. This method was used for recursively searching for files and directories that match the given search_term. This method returns an iterator, which yields a path object for each matching file or directory. This provides a memory-efficient way for searching through directory structures. It can include wildcards, as used in this program, like * or ?.
- argparse: This library is used for extracting the arguments given as an input by the user. This library was used because it also provides an argument "--help" which can be used by the user to get additional information regarding the usage of an argument. It also provides in-built error-handling, which helps to gracefully handle errors and display informative errormessages. It also provides flexibility in argument definition. 
- time: This was used to measure the time taken to perform the search operation. This was very helpful in assessing the performance of the search function.

## Flow of Control
- User runs the command
```bash
python3 -m Python_Challenge
```
- Python looks for a folder named Python_Challenge in the current directory.
- Python looks for a file named `__main__.py` inside the Python_Challenge folder.
- `main.py` file contains the CLI logic for displaying the welcome message and instructions for performing search. It parses command-line arguments (using argparse), and calls `mini_challenge.py`.
- `mini_challenge.py` receives the arguments, performs the search, and prints the results.

## Edge Cases
- Empty input in CLI
- No results for the given search_term
- Missing search_term
- Single character search_term
- Wrong argument name
- Using --ext with --only-dir
- Missing argument while using --ext

## Opportunities
The following are some features which could be added or alternate libraries that could be used:
- os library. Using this would change the approach to perform the search operation.
- sys library. This can be used as an alternative to argparser library, used for extracting different arguments as passed by the user through the CLI.
- Case-insensitive search could be performed.
- The program can be converted into a package, which could then be exported toany other device. This way any user can use this search functionality.
