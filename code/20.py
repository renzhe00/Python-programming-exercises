def func(n):
    i = 0
    while i<n:
        j = i
        i += 1
        if j%7==0:
            yield j

a = func(100)
try:
    while True:
        print(next(a))
except StopIteration:
    pass