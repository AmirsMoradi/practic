import pandas as pd
import numpy as np


data = {
    "name": ["Amir", "sara", "M0hsen", "hamid", "Shiva", "sara", None, "AMIR", "shiva "],
    "age": [25, 28, 999, 14, np.nan, 28, 30, -5, 14],
    "salary": [5000, 3000, 2000, None, 1000000, 3000, 2800, 5000, 4000],
    "city": ["Tehran", "Mashhad", "tehran", None, "shiraz", "unknown", "Qom", "Tehran", "shiraz"]
}


df = pd.DataFrame(data)
print(data)
print(df.isnull().sum())
df =df.dropna(subset=['salary',"name"])
df["name"] = df["name"].str.strip().str.lower()
try:
    if "m0hsen"in df.values:
        df["name"] = df["name"].str.replace('m0hsen',"mohsen")

    else :
        raise ValueError("not found the name ")

except Exception as e:
    print("programm have error")

df = df[(df["age"]>=10) & (df["salary"]<50000)]
df["city"] = df["city"].str.strip().str.lower()


df =df.drop_duplicates()


df.to_csv("clean.csv",index=False)
print("successfully saved")