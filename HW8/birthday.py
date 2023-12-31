from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    for user in users:
        
        user_name = user['name'].split()[0]
        weekday_birth = user['birthday'].strftime('%A')
        users = {}
        if weekday_birth not in users:
            users[weekday_birth] = []
        users[weekday_birth].append(user_name)
        
    first_day = datetime(year=2023, month=12, day=31)
    last_day = (6 - first_day.weekday()) + first_day.weekday()
    
    
    print(first_day, last_day)
    # return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", 
         "birthday": datetime(1976, 1, 1).date()},
    ]

    # result = get_birthdays_per_week(users)
    # print(result)
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
    get_birthdays_per_week(users)
