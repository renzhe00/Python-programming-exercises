def fn(n):
    if n==0:
        return 0
    else:
        return fn(n-1)+100

n = int(input())
print(fn(n))