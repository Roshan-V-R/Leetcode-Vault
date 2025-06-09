s = "abcd"
t = "abcde"
from collections import Counter
count_s = Counter(s)
count_t = Counter(t)

for ch in count_t:
    if count_t[ch] != count_s.get(ch,0):
        print(ch)