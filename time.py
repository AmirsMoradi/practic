import datetime


def real_time():
    now = datetime.datetime.now()
    print(now)


def calculate_age():
    birth_str = input("Enter your birth date and time (YYYY-MM-DD HH:MM:SS): ")
    birth_datetime = datetime.datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    delta = now - birth_datetime
    print(delta)


real_time()
calculate_age()