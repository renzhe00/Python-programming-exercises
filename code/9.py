lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
for s in lines:
    print(s)