import datetime

def calculate_set(birthday_str):
    birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')
    today = datetime.date.today()
    age = today.year - birthday.year-((today.month, today.day) < (birthday.month, birthday.day))
    return age

birthday_str = input("Enter your birthday: ")
print(calculate_set(birthday_str))