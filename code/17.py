balance = 0
while True:
    s = input()
    if not s:
        break
    value = s.split(' ')
    operation = value[0]
    amount = int(value[1])
    if operation == 'D':
        balance += amount
    elif operation == 'W':
        balance -= amount
    else:
        pass

print(balance)