import  pandas as pd
import numpy as np


data = {
    "name": ["Amir", "Sara", "Mohsen", "Hamid", "Shiva", "Sara", "Ali", "Amir", "Shiva"],
    "age": [25, 28, 45, 14, 33, 28, 39, 25, 33],
    "salary": [5000, 3000, 12000, 1500, 4000, 3000, 10000, 5000, 4000],
    "city": ["Tehran", "Mashhad", "Tehran", "Tabriz", "Shiraz", "Mashhad", "Tehran", "Tehran", "Shiraz"]
}
df = pd.DataFrame(data)
print(df)

mean = df["salary"].mean()
print(mean)
medi = df["salary"].median()
print(medi)
filtererd =df[(df["age"]<=20)&(df["age"]<=40)]


print(filtererd)

df.to_csv("selected_people.csv",index=False)
print("success")