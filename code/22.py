freq = {}
lines = input()
for word in lines.split(' '):
    freq[word] = freq.get(word, 0)+1

for word in sorted(freq.keys()):
    print('{0}:{1}'.format(word, freq[word]))