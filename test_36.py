grades = [18.5, 12.75, 9.0, 16.25, 19.75, 7.5, 20.0, 10.25]


for i in grades:
    if i > 17:
        print("grate:",i)
    elif i > 10 and i < 17:
        print("ok:",i)
    elif i < 10:
        print("filed:",i)
        
    else:
        print("finish")
