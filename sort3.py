import os
import shutil
import sys

def remove_folders(path_folder):
    for (root, dirs, files) in os.walk(path_folder, topdown=True):
        print(root)
        print(dirs)
        print(files)
        for dir in dirs:
            try:
                os.rmdir(dir)
            except OSError:
                print('Folder not empty')
                pass

# def sort_files(directory):
#     file_formats = {
#         'images': ['jpeg', 'png', 'jpg', 'svg'],
#         'videos': ['avi', 'mp4', 'mov', 'mkv'],
#         'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
#         'musics': ['mp3', 'ogg', 'wav', 'amr'],
#         'archives': ['zip', 'gz', 'tar']
#     }

    # Create subdirectories for each file type
    # for category in file_formats:
    #     try:
    #         category_folder = os.path.join(directory, category)
    #         os.makedirs(category_folder, exist_ok=True)
    #     except RecursionError:
    #         pass

    # Traverse the directory and move files to their respective folders
    # for filename in os.listdir(directory):
    #     file_path = os.path.join(directory, filename)
        
    #     if os.path.isdir(file_path):
    #         sort_files(file_path)
    #         try:
    #             os.rmdir(file_path)
    #             print(f"Removed empty folder: {file_path}")
    #         except OSError:
    #             pass

    #     elif os.path.isfile(file_path):
    #         shutil.move(file_path, 'C:\\Users\\harbazr\\Repositoreies\\GO_IT_RHA\\HW6\\test_garbage_folder_etalon')
            # _, file_extension = os.path.splitext(filename)
            # file_extension = file_extension[1:].lower()

            # for category, extensions in file_formats.items():
            #     if file_extension in extensions:
            #         category_folder = os.path.join(directory, category)
            #         shutil.move(file_path, os.path.join(category_folder, filename))
            #         break

if __name__ == "__main__":
    # folder_path = input("Enter the path of the folder to sort: ")
    folder_path = sys.argv[1]
    # if os.path.isdir(folder_path):
    #     sort_files(folder_path)
    #     print("Files sorted successfully.")
    # else:
    #     print("Invalid directory path.")
    remove_folders(folder_path)
    # sort_files(folder_path)