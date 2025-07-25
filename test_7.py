import pandas as pd


df=pd.read_csv("name")


mean_age =df.groupby("name")["age"].mean()
print(mean_age)
mean_salary = df.groupby("name")["salary"].mean()
print(mean_salary)