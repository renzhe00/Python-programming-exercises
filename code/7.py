dims = [int(x) for x in input().split(',')]
rowNum = dims[0]
colNum = dims[1]
value = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        value[row][col] = row*col

print(value)