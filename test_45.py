name = input("Enter your name: ")
st = 0
nu = 0
sp = 0
da = 0
for i in name:
    if i.isalpha():
        st += 1
    elif i.isdigit():
        nu += 1
    elif i.isspace():
        sp += 1
    else:
        da += 1

print("Number of letters:", st)
print("Number of digits:", nu)
print("Number of spaces:", sp)
print("Number of other characters:", da)

