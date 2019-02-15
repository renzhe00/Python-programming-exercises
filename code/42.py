tp = (1,2,3,4,5,6,7,8,9,10)
l = list()
for i in tp:
    if i%2==0:
        l.append(i)

print(tuple(l))