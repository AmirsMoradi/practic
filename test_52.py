
scores = [15.5, 18, 9, 14, 20, 8, 16.5, 12, 13.5, 7]
scores.append(17.25)
hight_number = max(scores)
index_hight =scores.index(hight_number)
print("index",index_hight)
print("hight_number",hight_number)
new_list = []
for i in scores:
    if i >= 10:
        new_list.append(i)
print(new_list)
avrege = sum(new_list)/len(new_list)
print("average:",avrege)
sort = sorted(scores)
print(sort)
count = 0
for i in scores:
    if i >= 15:
        count += 1
print("Numbers greater than 15:",count)
scores.reverse()