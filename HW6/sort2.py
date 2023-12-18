import os
import shutil
import zipfile
import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

def normalize(file_name):
    # Translate characters 
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    translated = file_name.translate(TRANS)
    
    # Replace all not A-Za-z0-9. characters to '_'
    normalized_file_name = re.sub(r'[^A-Za-z0-9.]', '_', translated)
    return normalized_file_name

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # Delete ignored folders from list
        dirs[:] = [d for d in dirs if d not in ['archives', 'video', 'audio', 'documents', 'images', 'other']]
        
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file)
            file_extension = file_extension[1:].upper()

            new_file_name = normalize(file)

            if file_extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
                category = 'images'
            elif file_extension in ['AVI', 'MP4', 'MOV', 'MKV']:
                category = 'video'
            elif file_extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
                category = 'documents'
            elif file_extension in ['MP3', 'OGG', 'WAV', 'AMR']:
                category = 'audio'
            elif file_extension in ['ZIP', 'GZ', 'TAR']:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(folder_path, 'archives', os.path.splitext(file)[0]))
                continue
            else:
                category = 'other'

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            new_file_path = os.path.join(category_folder, new_file_name)
            shutil.move(file_path, new_file_path)

            print(f"Moved: {file_path} -> {new_file_path}")

        for dir_path in dirs:
            dir_full_path = os.path.join(root, dir_path)
            # Recursive function to open subfolders
            process_folder(dir_full_path)

            # Delete empty folder
            try:
                os.rmdir(dir_full_path)
                print(f"Removed empty folder: {dir_full_path}")
            except OSError:
                pass  # Folder is not empty

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)