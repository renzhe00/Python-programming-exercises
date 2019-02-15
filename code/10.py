words = [x for x in input().split(' ')]
words = sorted(set(words))
print(' '.join(words))