import os
import shutil
from pathlib import Path

def organize_directory(directory_path):
    """
    Organizes files in the given directory into subfolders based on their file extensions.
    """
    path = Path(directory_path)
    
    if not path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Define file type categories
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".tar", ".rar", ".7z"],
        "Scripts": [".py", ".js", ".sh", ".bat"],
    }

    for item in path.iterdir():
        if item.is_file():
            file_ext = item.suffix.lower()
            moved = False
            
            for category, exts in extensions.items():
                if file_ext in exts:
                    dest_dir = path / category
                    dest_dir.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_dir / item.name))
                    print(f"Moved: {item.name} -> {category}/")
                    moved = True
                    break
            
            if not moved:
                dest_dir = path / "Others"
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_dir / item.name))
                print(f"Moved: {item.name} -> Others/")

if __name__ == "__main__":
    # Example usage: Organize the current directory or a specific folder
    target = input("Enter the directory path to organize (leave blank for current): ").strip()
    if not target:
        target = "."
    
    print(f"Organizing files in: {os.path.abspath(target)}...")
    organize_directory(target)
    print("Cleanup complete!")
