from datetime import date, datetime


def get_birthdays_per_week():
    # Реалізуйте тут домашнє завдання
    # for user in users:
    #     current_day = date.today().strftime("%A")
    current_day = date.today().strftime("%A") + 1
    print(current_day)
    # return users


if __name__ == "__main__":
    # users = [
    #     {"name": "Jan Koum", 
    #      "birthday": datetime(1976, 1, 1).date()},
    # ]

    # result = get_birthdays_per_week(users)
    # print(result)
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
    get_birthdays_per_week()
