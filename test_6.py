import pandas as pd


df = pd.read_csv("name")

young = df[df["age"]<30]
print("youngest people:\n",young)
group_salary =df.groupby("name")["salary"].mean()
print(group_salary)
young.to_csv("youngest.csv")

