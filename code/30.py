def maxLen(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1<l2:
        print(s2)
    elif l1==l2:
        print(s1)
        print(s2)
    else:
        print(s1)

maxLen('www', 'qqq')
maxLen('q', 'www')