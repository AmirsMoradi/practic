import datetime



def calculate_time(time_str):
  try:
    time = datetime.datetime.strptime(time_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    if time<=today:
        return "این تاریخ در گذشته یا امروز است "

    delta = time - today
    return f"{delta.days} این تاریخ در اینده است "
  except ValueError:
      return" فرمت تاریخ معتبر نیست. لطفاً به صورت YYYY-MM-DD وارد کنید."

time_str =input("enter your time:")
print(calculate_time(time_str))