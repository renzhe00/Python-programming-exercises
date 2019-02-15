def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    for v in d.values():
        print(v, end=' ')

dicts(1, 20)