def printList(a, b):
    if b-a<5:
        return
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(l[5:])

printList(1,20)