import os
import shutil
import re
import sys
import pathlib

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

file_formats = {
    'image' : ['jpeg', 'png', 'jpg', 'svg'],
    'video' : ['avi', 'mp4', 'mov', 'mkv'],
    'document' : ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'music' : ['mp3', 'ogg', 'wav', 'amr'],
    'archive' : ['zip', 'gz', 'tar']
}

# Function normalize() get input str and return str
def normalize(file_name):
    # Translate characters 
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    translated = file_name.translate(TRANS)
    
    # Replace all not A-Za-z0-9. characters to '_'
    normalized_file_name = re.sub(r'[^A-Za-z0-9.]', '_', translated)
    return normalized_file_name


def sort(path):
    list_dir = os.listdir(path)
    print(list_dir)
    for el in list_dir:
        if os.path.isdir(el):
            new_dir = 
            
            

# print(sort('C:\Users\ROMAN\Downloads'))

# def walk(path, prev_list_dir):
#     print(prev_list_dir)
#     print(os.getcwd())
#     os.chdir(path)
#     list_dir = list(filter(os.path.isdir, os.listdir()))
    
#     for el in list_dir:
#         walk(fr'{path}\{el}', list_dir.remove(el))

if __name__ == "__main__":
    folder_path = sys.argv[1]
    sort(folder_path)

