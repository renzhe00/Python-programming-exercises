l = [12,24,35,70,88,120,155]
new_l = [x for (i, x) in enumerate(l) if i%2!=0]
print(new_l)