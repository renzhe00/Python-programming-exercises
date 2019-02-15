def printTuple(a, b):
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(tuple(l))

printTuple(1,20)