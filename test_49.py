scores = [15.5, 18, 9, 14, 20, 8, 16.5, 12, 13.5, 7]
v = sum(scores)/len(scores)
new_list = []
print(v)
for i in scores:
    if i < v :
        new_list.append(i)
print("little of the average :",new_list)
