def new(name,price,number):
    if number >10 :
        discount = 30
    elif number >5 :
        discount = 20
    elif number >2 :
        discount = 10
    elif number >1 :
        discount = 5

    discount_amount = discount * price / 100
    final_price = price - discount_amount
    return final_price , discount_amount
