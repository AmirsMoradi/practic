name = input("Enter your name: ")
st = 0
nu = 0
for i in name:
    if i.isdigit():
        nu += 1
    elif i.isalpha():
        st += 1
print("number of the string in name :",st)
print("number of the number in name :",nu)