import re

s = input()
r = re.findall(r'\d+', s)
print(r)