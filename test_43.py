score = [20, 17, 18, 19, 10, 4, 6, 7.5, 1, 2.5, 13, 19, 17.5]
under_ten = []
for s in score:
    if s < 10 :
        under_ten.append(s)
print("score under ten:",len(under_ten))

print(score)
for i in score:
    if i > 10:
        print(i)

print("average:",sum(score)/len(score))