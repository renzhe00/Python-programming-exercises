values = [int(x) for x in input().split(',')]
numbers = [str(x*x) for x in values if x%2!=0]

print(','.join(numbers))