import re

def find_all_links(text):
    result = []
    iterator = re.finditer(r"(http[s]://\w+\.\w+\.\w{3})", text)
    for match in iterator:
        result.append(match.group())
    return result

print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '))

# https://bulldogjob.pl/readme/samouczek-regex-sciagawka-z-przykladami
# https://docs.python.org/3/library/re.html
# https://ggoralski.gitlab.io/python-wprowadzenie/czesc_ii/2_01-regex/
# https://habr.com/ru/articles/349860/