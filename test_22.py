price = int(input("enter price:"))
tax = int(input("enter tax rate:"))
final = price + (price * tax / 100)

print(f"the tax is{final:2f}")
