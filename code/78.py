import time

start = time.time()
for _ in range(100):
    a = 1+1
stop = time.time()
print((stop - start)*1000)