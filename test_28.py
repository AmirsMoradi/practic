def calculate (price):
    if price > 5000:
        discount = price * 0.20
    else :
        discount = price * 0.10
    final_price = price - discount
    return final_price


print(calculate(70000))
