from pathlib import Path
import argparse
import time

def searching(pattern, matches, only_file, only_dir, ext, root):
    try:
        p = Path('/') if root else Path('/home')
        for path in p.rglob(pattern):
            try:
                if str(path).startswith("/proc"):
                    continue
                if ext and not str(path).endswith(ext):
                    continue
                if only_file and not path.is_file():
                    continue
                if only_dir and not path.is_dir():
                    continue

                matches.append(path)

            except (PermissionError, FileNotFoundError, OSError):
                continue
    except (PermissionError, FileNotFoundError, OSError):
        pass

    return matches

def main():

    parser = argparse.ArgumentParser(description="Search for files or directories.")
    parser.add_argument("search_term", help="The name of the file or directory to be searched.")
    parser.add_argument("--only-file", action="store_true", help="Only look for files.")
    parser.add_argument("--only-dir", action="store_true", help="Only look for directories.")
    parser.add_argument("--ext", help="Only return results with this extension. Eg: Use py for only python file results.")
    parser.add_argument("--only-name", action="store_true", help="Only displays names of the files/directories.")
    parser.add_argument("--root", action="store_true", help="Searches from the root directory.")
    
    args = parser.parse_args()

    if args.ext and args.only_dir:
        return print("Error: You cannot have an extension for a directory!!!")
    
    if len(args.search_term) < 2:
        return print("Error: Enter at least two characters as search term!!!")

    pattern = args.search_term
    if "*" not in pattern and "?" not in pattern:
        pattern = f"*{pattern}*"

    matches = []

    start_time = time.perf_counter()
    res = searching(pattern, matches, args.only_file, args.only_dir, args.ext, args.root)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    if len(res) > 0:
        print(f"\nFound {len(matches)} matches in {execution_time:.2f} seconds.\n")
        for result in res:
            if args.only_name:
                print(result.name)
            else:
                print(result)
    else:
        print("\nSorry, No matches found!!!")

if __name__ == "__main__":
    main()