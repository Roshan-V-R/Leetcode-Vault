def sum(nums,k):
    count = 0
    current_sum = 0
    prefix_counts = {0:1}
    for num in nums:
        current_sum = current_sum+num
        if current_sum - k in prefix_counts:
            count = count + prefix_counts[current_sum - k]
        prefix_counts[current_sum] = prefix_counts.get(current_sum,0)+1
    return count
