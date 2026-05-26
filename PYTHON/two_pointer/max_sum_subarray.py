def max_sum_subarray(nums, k):
    window_sum = 0
    left = 0
    right = k - 1
    for i in range(left, right+1):
        window_sum += nums[i]
    maxi = window_sum
    while right < len(nums) - 1:
        right += 1
        window_sum = window_sum - nums[left] + nums[right]
        if maxi < window_sum:
            maxi = window_sum
        left += 1
    return maxi

nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # expected: 9