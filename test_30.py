def new_kala(name,price):
    if price >15000 :
        discount = 20
    else :
        discount = 10

    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

name = input("Enter your name of kala: ")
price = float(input("Enter your price of kala: "))

new_kala(name, price)
print(f"name of kala {name}")
print(f"price of kala {price}")
