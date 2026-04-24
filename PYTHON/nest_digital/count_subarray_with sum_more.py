def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    count = 0
    window_sum = sum(nums[:M])
    if window_sum == k :
        count += 1
    for j in range(M,len(nums)):
        window_sum += nums[j] - nums[j-M]
        if window_sum == k:
            count += 1   
    return count

nums = [2, -1, 2, 1, -2, 3]
k = 3
M = 2
print(countSubarraysWithSumAndMaxAtMost(nums,k,M))