import os
import shutil

# Extension mappings
EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi']
}

def organize_folder(path):
    if not os.path.isdir(path):
        print(f"Path '{path}' is not a directory.")
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
            
        file_ext = os.path.splitext(item)[1].lower()
        moved = False
        
        for folder, ext_list in EXTENSIONS.items():
            if file_ext in ext_list:
                dest_folder = os.path.join(path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(dest_folder, item))
                print(f"Moved {item} to {folder}")
                moved = True
                break
        
        if not moved:
            others_folder = os.path.join(path, 'Others')
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(others_folder, item))
            print(f"Moved {item} to Others")

if __name__ == "__main__":
    target = input("Enter path to organize (or '.' for current): ")
    organize_folder(target)
