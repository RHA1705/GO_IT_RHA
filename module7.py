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
def solve_riddle(riddle, word_length, start_letter, reverse=False):
# 1. Znaleźć start_letter in riddle.
# 2. Odliczyć word_lenght od riddle[start_letter]
# 4. Zwrócić wynik
    if reverse is False:
        x = riddle.index(start_letter)
        result = riddle[x:x+word_length]
        return result
    if reverse is True:
        x = riddle.index(start_letter)
        result = riddle[x:x-word_length:-1]
        return result
    return []
print(solve_riddle('mi1powerpret', 5, 'p'))
