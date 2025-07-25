import datetime


def calculate_time(birthday_str):
   try:
        birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')
        today = datetime.date.today()
        age = today.year - birthday.year-((today.month, today.day) < (birthday.month, birthday.day))
        return age
   except ValueError:
        return ("invalid birthday")

birthday_str = input("Enter your birthday: ")
print("answer",calculate_time(birthday_str))