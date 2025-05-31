nums = [1,1,1,2,2,3]
k = 2
from collections import Counter
count = Counter(nums)

bucket = [[] for _ in range(len(nums)+1)]
for num,freq in count.items():
    bucket[freq].append(num)

result = []
for i in range(len(bucket)-1,-1,-1):
    for num in bucket[i]:
        result.append(num)
        if len(result) == k:
            print(result)