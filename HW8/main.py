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

today = date.today()
sunday = 6 - today.weekday() % 6
date_sunday = date(today.year, today.month, today.day + sunday)
print(sunday)
print(date_sunday)
days = []
for day in range(today.weekday(), date_sunday.weekday()):
    day = date(today.year, today.month, today.day + day).strftime('%A')
    days.append(day)

print(days)
