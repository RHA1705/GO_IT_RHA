import os
import shutil
import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

def normalize(file_name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    translated = file_name.translate(TRANS)
    normalized_file_name = 
    return translated

print(normalize('зобр!@#.png'))

# def walk(path, prev_list_dir):
#     print(prev_list_dir)
#     print(os.getcwd())
#     os.chdir(path)
#     list_dir = list(filter(os.path.isdir, os.listdir()))
    
#     for el in list_dir:
#         walk(fr'{path}\{el}', list_dir.remove(el))

# def main():
#     pass

# if __name__ == "__main__":
#     main()
