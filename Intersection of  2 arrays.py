def intersection(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    intersected = set1 & set2
    return print(list(intersected))

nums1 = [1,2,2,1]
nums2 = [2,2]
intersection(nums1,nums2)

#Manual method using hashmap
def inter(nums3,nums4):
    freq = {}
    res = []

    for nums in nums3:
        freq[nums] = True
    for num in nums4:
        if freq.get(num, False):
            res.append(num)
            freq[num] = False

    return res
