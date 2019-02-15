value = []
s = [x for x in input().split(',')]
for e in s:
    dec = int(e, base=2)
    if dec%5 == 0:
        value.append(e)

print(','.join(value))