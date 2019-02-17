string = input()
d = dict()
for s in string:
    d[s] = d.get(s, 0)+1

print('\n'.join(['{0},{1}'.format(k, v) for (k, v) in d.items()]))