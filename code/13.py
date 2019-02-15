s = input()
d = {"LETTERS":0, "DIGITS":0}
for i in s:
    if i.isdigit():
        d['DIGITS']+=1
    elif i.isalpha():
        d['LETTERS']+=1
    else:
        pass

print('LETTERS: {0}\nDIGITS: {1}'.format(d['LETTERS'], d['DIGITS']))