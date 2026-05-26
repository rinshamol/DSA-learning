def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))   # expected: 3
print(binary_search(nums, 6))   # expected: -1