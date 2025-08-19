from pathlib import Path
import argparse
import time

# This function searches for files or directories based on user-defined criteria.
def searching(pattern, matches, only_file, only_dir, ext, root):
    try:
        # Set the starting path based on whether the search is from the root or home directory.
        p = Path('/') if root else Path('/home')
        for path in p.rglob(pattern):
            try:
                # Skip the /proc directory as it contains virtual files that are not real files on disk.
                # This is important to avoid unnecessary processing and was also leading to unncessary FileNotFoundError errors.
                if str(path).startswith("/proc"):
                    continue

                # Check if the path matches the extension, file type, and directory type criteria.
                if ext and not str(path).endswith(ext):
                    continue
                if only_file and not path.is_file():
                    continue
                if only_dir and not path.is_dir():
                    continue

                # If all criteria are met, add the path to the matches list.
                matches.append(path)

            # Handle exceptions that may occur while accessing the file system.
            except (PermissionError, FileNotFoundError, OSError):
                continue
    except (PermissionError, FileNotFoundError, OSError):
        pass

    return matches

def main():
    # Set up the argument parser to handle command line arguments used for search.
    parser = argparse.ArgumentParser(description="Search for files or directories.")
    parser.add_argument("search_term", help="The name of the file or directory to be searched.")
    parser.add_argument("--only-file", action="store_true", help="Only look for files.")
    parser.add_argument("--only-dir", action="store_true", help="Only look for directories.")
    parser.add_argument("--ext", help="Only return results with this extension. Eg: Use py for only python file results.")
    parser.add_argument("--only-name", action="store_true", help="Only displays names of the files/directories.")
    parser.add_argument("--root", action="store_true", help="Searches from the root directory.")

    args = parser.parse_args()

    # If both --only-file and --only-dir are set, it is an error as directory cannot have an extension.
    if args.ext and args.only_dir:
        return print("Error: You cannot have an extension for a directory!!!")
    
    # Need at least two characters in the search term to avoid unnecessary processing.
    if len(args.search_term) < 2:
        return print("Error: Enter at least two characters as search term!!!")

    # If the search term does not contain wildcards, add them to ensure proper matching.
    pattern = args.search_term
    if "*" not in pattern and "?" not in pattern:
        pattern = f"*{pattern}*"

    # Initialize the matches list to store the results.
    # This will hold the paths of files or directories that match the search criteria.
    matches = []

    # Start the search and measure the execution time.
    # This will help in understanding how long the search took.
    start_time = time.perf_counter()
    res = searching(pattern, matches, args.only_file, args.only_dir, args.ext, args.root)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Print the results based on the user's preferences.
    if len(res) > 0:
        print(f"\nFound {len(matches)} matches in {execution_time:.2f} seconds.\n")
        for result in res:
            # If --only-name is specified, it will only print the name of the file or directory.
            if args.only_name:
                print(result.name)
            # Otherwise, it will print the full path of the file or directory.
            else:
                print(result)
    else: # If no matches are found, print a message indicating that.
        print("\nSorry, No matches found!!!")

if __name__ == "__main__":
    main()