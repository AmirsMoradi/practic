scores = [20, 17, 18, 19, 10, 4, 6, 7.5, 1, 2.5, 13, 19, 17.5]
new_list =[]
v = sum(scores)/len(scores)
print(v)
for i in scores:
    if i > v :
        new_list.append(i)
print(new_list)
