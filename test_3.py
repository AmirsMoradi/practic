import pandas as pd

df = pd.read_csv("test")
print(df)

print("average price:",df["price"].mean())