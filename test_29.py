
def kala(name, price):
    if price > 10000:
        discount = 25
    elif price > 5000:
        discount = 10
    else:
        discount = 5

    discount_rate = price * discount / 100
    final_price = price - discount_rate

    return final_price, discount_rate

name = input("Enter your name: ")
price = float(input("Enter the price: "))

final, discount_value = kala(name, price)

print(f"Product name: {name}")
print(f"Discount amount: {discount_value:.2f}")
print(f"Final price: {final:.2f}")
