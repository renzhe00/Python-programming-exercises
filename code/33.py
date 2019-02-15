def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    print(d)

dicts(1, 20)