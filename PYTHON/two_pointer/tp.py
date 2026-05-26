def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return -1


nums = [1, 3, 5, 7, 9]
target = 10
print(two_sum_sorted(nums, target))  # expected: [0, 4] (1+9=10)