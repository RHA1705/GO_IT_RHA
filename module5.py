import re

def find_word(text, word):
    result = False
    first_index = None
    last_index = None
    search_string = word
    string = text
    
    searching = re.search(word, text)
    
    if searching:
        result = True
        search_string = searching.group()
        indexes = searching.span()
        first_index = indexes[0]
        last_index = indexes[1]
        
    result_dict = {'result': result, 'first_index': first_index, 'last_index': last_index, 'search_string': search_string, 'string': string}
    return result_dict    
        
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))