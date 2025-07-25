import pandas as pd

data =pd.read_csv("name")

df =pd.DataFrame(data)


diffrent =df.query("age < 30 and salary > 3000")
print(diffrent)
diffrent.to_csv("diffrent_2.csv")