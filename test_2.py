import pandas as pd

data = {"coin":["Bitcoin","Ethereum","Dogecoin"],
        "price":[5000,120000,6000],
        "volume":[10000,2000,3000]}


df = pd.DataFrame(data)
df.to_csv("test",index=False)