def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
l = [str(fib(x)) for x in range(0, n+1)]
print(','.join(l))