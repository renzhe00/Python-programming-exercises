n = int(input())
sum = 0.0
for i in range(1,n+1):
    sum += float(i/(i+1.0))

print('%.2f' % sum)