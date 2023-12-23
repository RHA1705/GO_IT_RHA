import os
import shutil
import sys

def sort_files(directory):
    file_formats = {
        'image': ['jpeg', 'png', 'jpg', 'svg'],
        'video': ['avi', 'mp4', 'mov', 'mkv'],
        'document': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
        'music': ['mp3', 'ogg', 'wav', 'amr'],
        'archive': ['zip', 'gz', 'tar']
    }

    # Create subdirectories for each file type
    for category in file_formats:
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

    # Traverse the directory and move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isdir(file_path):
            sort_files(file_path)
            try:
                os.rmdir(file_path)
                print(f"Removed empty folder: {file_path}")
            except OSError:
                pass

        elif os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:].lower()

            for category, extensions in file_formats.items():
                if file_extension in extensions:
                    category_folder = os.path.join(directory, category)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    break

if __name__ == "__main__":
    # folder_path = input("Enter the path of the folder to sort: ")
    folder_path = sys.argv[1]
    if os.path.isdir(folder_path):
        sort_files(folder_path)
        print("Files sorted successfully.")
    else:
        print("Invalid directory path.")
    
    # sort_files(folder_path)