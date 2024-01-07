from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    week_birthdays = {}
    for user in users:
        user_name = user['name'].split()[0]
        birthday = user['birthday']
        weekday_birth = birthday.strftime('%A')
        print(user_name, weekday_birth)
        today = date(2024, 1, 8)
        sunday = 6 - today.weekday()
        date_sunday = date(today.year, today.month, today.day + sunday)
        days = []
        names = []
        for day in range(today.weekday(), date_sunday.weekday() + 1):
            day = date(today.year, today.month, day + 1).strftime('%A')
            print(date_sunday.weekday())
            days.append(day)
            if weekday_birth == day:
                names.append(user_name)
                week_birthdays.update({day : names})
        print(days)
    
    print(week_birthdays)
    # return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", 
         "birthday": datetime(1976, 1, 1).date()},
        {"name": "Roman Harbazh", 
         "birthday": datetime(2024, 1, 7).date()},
        {"name": "Olenka Harbazh", 
         "birthday": datetime(2024, 1, 10).date()},
        {"name": "Sofia Harbazh", 
         "birthday": datetime(2024, 1, 10).date()}
    ]

    # result = get_birthdays_per_week(users)
    # print(result)
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
    get_birthdays_per_week(users)
