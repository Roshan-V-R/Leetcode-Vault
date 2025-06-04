def firstbadsearch(n,b):
    l = 0
    r = n

    while l <= r:
        mid = (l+r) // 2
        if n[mid] == b:
            return b
        else:
            l = mid + 1
    return l
