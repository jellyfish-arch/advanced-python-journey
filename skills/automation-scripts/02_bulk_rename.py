import os
from pathlib import Path

def bulk_rename(directory, prefix="", suffix="", replace_str=None, new_str=""):
    """
    Renames files in a directory by adding prefixes, suffixes, or replacing parts of the filename.
    """
    path = Path(directory)
    
    if not path.is_dir():
        print(f"Error: {directory} is not a valid directory.")
        return

    count = 0
    for item in path.iterdir():
        if item.is_file():
            # Skip the script itself if it's in the same directory
            if item.name == os.path.basename(__file__):
                continue
                
            old_name = item.stem
            extension = item.suffix
            
            # Apply transformations
            new_name = old_name
            if replace_str:
                new_name = new_name.replace(replace_str, new_str)
            
            final_name = f"{prefix}{new_name}{suffix}{extension}"
            new_path = path / final_name
            
            try:
                item.rename(new_path)
                print(f"Renamed: {item.name} -> {final_name}")
                count += 1
            except Exception as e:
                print(f"Failed to rename {item.name}: {e}")

    print(f"\nSuccessfully renamed {count} files.")

if __name__ == "__main__":
    dir_to_rename = input("Enter directory path: ").strip()
    if not dir_to_rename: dir_to_rename = "."
    
    pre = input("Enter prefix (optional): ")
    suf = input("Enter suffix (optional): ")
    rep = input("Text to replace (optional): ")
    wit = ""
    if rep:
        wit = input(f"Replace '{rep}' with: ")

    bulk_rename(dir_to_rename, prefix=pre, suffix=suf, replace_str=rep, new_str=wit)
