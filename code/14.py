s = input()
d = {'UPPER CASE':0, 'LOWER CASE':0}
for i in s:
    if i.isupper():
        d['UPPER CASE']+=1
    elif i.islower():
        d['LOWER CASE']+=1
    else:
        pass

print('UPPER CASE: {0}\nLOWER CASE: {1}'.format(d['UPPER CASE'], d['LOWER CASE']))