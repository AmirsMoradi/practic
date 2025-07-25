price =float(input("Enter your price :"))
tax_rate =float(input("Enter your tax rate :"))

tax_amount = price * tax_rate /100
final_price = price + tax_amount

print(f"your product price is {final_price:2f}toman")
print(f"tax amount is ({tax_rate})%{tax_amount:2f}")
print(f"final price {final_price:2f}")

