def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

x = int(input())
print(fact(x))