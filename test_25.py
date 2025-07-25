
def calculate(name_commodity,price):


 if price  >5000:
    discount_rate = 20
 else:
    discount_rate = 10
 discount_amount  = price * discount_rate /100
 final_price = price - discount_amount


# print(f"name of commodity {name_commodity} \n  your discount rate {discount_rate:.2f} \n  your discount amount {discount_amount:.2f}"
 #
 print(f"final price {final_price:.2f}")
 return final_price



calculate(5000,200)