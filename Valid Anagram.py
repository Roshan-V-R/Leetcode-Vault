def anagram(s,t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch,0) + 1
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    p = print(True)

    return p





anagram('earth','heart')