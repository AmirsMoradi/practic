import pandas as pd



df = pd.read_csv("name")

print(df)


print("if name is amir:",df[df["name"]=="amir"])