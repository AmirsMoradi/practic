grades = [17.5, 12.0, 18.75, 9.5, 20.0, 15.25, 13.0, 19.0]


print("max:",max(grades))
print("min",min(grades))
print("avg:",sum(grades)/len(grades))
for i in grades:
    if i > 10 :
        print("good",i)
    elif i > 18:
        print("excellent",i)
    elif i < 12:
        print("needs improvement",i)
