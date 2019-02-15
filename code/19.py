from operator import itemgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(',')))

print(sorted(l,key=itemgetter(0,1,2)))