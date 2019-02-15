import re

s = input().split(',')
correct = []
for e in s:
    if len(e)<6 or len(e)>12:
        continue
    if not re.search('[a-z]', e):
        continue
    elif not re.search('[0-9]', e):
        continue
    elif not re.search('[A-Z]', e):
        continue
    elif not re.search('[$#@]', e):
        continue
    correct.append(e)

print(','.join(correct))