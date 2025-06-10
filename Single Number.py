def single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

single([1,2,3,3,2,1,4])