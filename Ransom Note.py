def Note(word,letters):
    from collections import Counter
    count_w = Counter(word)
    count_l = Counter(letters)
    for char in count_w:
        if count_w[char] > count_l.get(char,0):
            return False
    return True


