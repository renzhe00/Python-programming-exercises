import math

c, h, values = 50, 30, []
items = [int(x) for x in input().split(',')]
for d in items:
    value = math.sqrt(2*c*float(d)/h)
    values.append(str(round(value)))

print(','.join(values))