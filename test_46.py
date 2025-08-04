number = []
odd_number =[]
even_number=[]
while True:
    nu = int(input("enter a number: "))
    if nu == 0:
        break
    number.append(nu)
    if nu % 2 == 0:
        even_number.append(nu)
    else :
        odd_number.append(nu)


print(number)
print("max number:",max(number))
print("min number:",min(number))
print("average number:",sum(number)/len(number))
print("odd number:",odd_number)
print("even number:",even_number)
