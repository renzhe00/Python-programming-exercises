import random

print(random.sample([x for x in range(100, 201) if x%2==0], 5))