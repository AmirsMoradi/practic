import pandas  as pd

data = {"name":["amir","mohsen","reza","hamid","shiva","sara"],
        "age":[25,37,12,14,26,14],
        "salary":[5000,2000,7000,3000,2000,3600]}


df =pd.DataFrame(data)
df.to_csv("name",index=False)

print(df)
print("average of mean:",df["age"].mean())
print(df["salary"].mean())
print(df["salary"].max())
print(df[df["salary"]>4500])
