grades = [17.5, 12.0, 18.75, 9.5, 20.0, 15.25, 13.0, 19.0]


good_grades =[]
excellent_grades =[]
weak_grades = []
average_grades =[]

good = 0
excellent =0
weak = 0
average = 0

for i  in grades:
    if i > 18 :
        excellent_grades.append(i)
        excellent +=1
    elif i >14 and i <18 :
        good_grades.append(i)
        good +=1
    elif i > 10 and i <14:
        average_grades.append(i)
        average +=1
    else :
        weak_grades.append(i)
        weak +=1
print(f"People who had excellent grades{excellent}",excellent_grades)
print(f"People who had good grades{good}",good_grades)
print(f"People who had average grades{average}",average_grades)
print(f"People who had weak grades{weak}",weak_grades)