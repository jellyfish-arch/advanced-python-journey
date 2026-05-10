import os
import sys

def bulk_rename(directory, prefix, extension):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    count = 1
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            new_name = f"{prefix}_{count}{extension}"
            source = os.path.join(directory, filename)
            destination = os.path.join(directory, new_name)
            
            os.rename(source, destination)
            print(f"Renamed: {filename} -> {new_name}")
            count += 1

if __name__ == "__main__":
    print("--- Bulk File Renamer ---")
    dir_path = input("Enter directory path: ")
    pref = input("Enter new prefix: ")
    ext = input("Enter file extension to target (e.g., .txt): ")
    
    if not ext.startswith('.'):
        ext = '.' + ext
        
    bulk_rename(dir_path, pref, ext)
