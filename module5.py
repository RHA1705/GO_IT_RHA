import re
def find_all_phones(text):
    result = re.findall(r"(\+380\(\d{2}\)\d{3}\-\d-\d{3}|\+380\(\d{2}\)\d{3}\-\d{2}-\d{2})", text)
    return result

print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))

# https://bulldogjob.pl/readme/samouczek-regex-sciagawka-z-przykladami
# https://docs.python.org/3/library/re.html
# https://ggoralski.gitlab.io/python-wprowadzenie/czesc_ii/2_01-regex/
# https://habr.com/ru/articles/349860/