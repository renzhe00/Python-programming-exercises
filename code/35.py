def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    for k in d.keys():
        print(k, end=' ')

dicts(1, 20)