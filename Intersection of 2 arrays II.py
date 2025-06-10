def intersection(nums1,nums2):
    from collections import Counter
    res = []
    count = Counter(nums1)
    for num in nums2:
        if num in count and count[num] > 0:
            res.append(num)
            count[num]-=1
    return res

