grades = [17.5, 12.0, 18.75, 9.5, 20.0, 15.25, 13.0, 19.0]


print(max(grades))
print(min(grades))
print("avg:",sum(grades)/len(grades))
excellent =0
good = 0
average = 0
weak = 0
for i in grades:
    if i > 18 :
        excellent +=1
        print("excellent",i)
    if i >14 and i <18 :
        good +=1
        print("good",i)
    if i >10 and i < 14 :
        average +=1
        print("average",i)
    if i < 10 :
        weak +=1
        print("weak",i)

print("Students with excellent grades:",excellent)
print("Good grades:",good)
print("Weak grades:",weak)
print("Students with average grades",average)