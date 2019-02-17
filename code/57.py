import re

address = input()
r = re.match(r'(\w+)@(\w+).(com)', address)
print(r.group(2))