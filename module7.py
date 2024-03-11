'''Task Nr 5'''
# def capital_text(s):
#     s = s.strip()
#     if s[0].isalpha():
#         s = s[0].upper() + s[1:]

#     for i in range(1, len(s)):

#         if s[i] == '.':
#             s = s[:i+2] + s[i+2].upper() + s[i+3:]
#         if s[i] == '!':
#             s = s[:i+2] + s[i+2].upper() + s[i+3:]
#         if s[i] == '?':
#             s = s[:i+2] + s[i+2].upper() + s[i+3:]

#     return s

# print(capital_text('    asdf. asd! asd? asd'))

'''Task Nr 6'''
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     try:
#         if reverse is False:
#             x = riddle.index(start_letter)
#             result = riddle[x:x+word_length]
#             return result
#         if reverse is True:
#             x = riddle.index(start_letter)
#             result = riddle[x:x-word_length:-1]
#             return result
#     except ValueError:
#         return ''
# print(solve_riddle('mi1powerpret', 5, 'p'))

'''Task Nr 7'''
# def data_preparation(list_data):
#     result = []
#     for l in list_data:
#         if len(l) > 0:
#             l_max = max(l)
#             l_min = min(l)
#             if len(l) > 2:
#                 l.remove(l_max)
#                 l.remove(l_min)
#             for i in l:
#                 result.append(i)
#     result.sort(reverse=True)
#     return result

# print(data_preparation([[1,2,3], [3,4], [5,6]]))

'''Task Nr 8'''
# import re

# def token_parser(s):
#     token = re.findall(r'\d+|\+|\-|\/|\*|\(|\)', s)
#     return token

# print(token_parser('123 + asde -  12345'))

'''Task Nr 9'''
def all_sub_lists(data):
    sublists = [[]]  # Починаємо з порожнього підсписку
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            sublists.append(data[i:j])    
    return sublists
print(all_sub_lists([1, 2, 3]))
