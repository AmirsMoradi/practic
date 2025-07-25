import pandas as pd

df = pd.read_csv("test")

mean_price = df['price'].mean()
high_prices = df[df['price'] > mean_price]

print("Coins with price above average:")
print(high_prices)
