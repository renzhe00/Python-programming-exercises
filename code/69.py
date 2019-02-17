def bin_search(l, element):
    bottom, top, index = 0, len(l)-1, -1
    while top>=bottom and index==-1:
        mid = int((top+bottom)/2)
        if l[mid]==element:
            index = mid
        elif l[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

l = [1,2,4,6,8,12,17,18,56]
print(bin_search(l, 1))
print(bin_search(l, 17))
print(bin_search(l, 56))