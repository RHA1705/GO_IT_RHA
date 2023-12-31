from datetime import date, datetime
# 
# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

today = datetime(year=2023, month=6, day=1)
future_year = today.month / 12
print(int(future_year))