name_commodity = input("Enter your name of commodity: ")
price = float(input("Enter your price: "))
tax_rate =float(input("Enter your tax rate: "))


tax_amount = price * tax_rate /100
final_price = price + tax_amount

print(f"name of commodity{name_commodity} \n tax amount = {tax_amount} \n final price = {final_price}")


