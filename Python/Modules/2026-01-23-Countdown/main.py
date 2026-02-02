import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 12, 3)
days_away = today - next_birthday

if today == next_birthday:
    print(random_message)
else:
    print("My next birthday is", days_away, "days away!")