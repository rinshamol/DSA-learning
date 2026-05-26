def first_and_last(nums, target):
    def first_position(nums, target):
        start, end = 0, len(nums) - 1
        result = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid      # save it
                end = mid - 1     # keep searching left
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return result
    
    def last_position(nums, target):
        start, end = 0, len(nums) - 1
        result = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid      # save it
                start = mid + 1     # keep searching left
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return result
    
    return [first_position(nums, target), last_position(nums, target)]

nums = [1, 3, 3, 3, 5, 7]
target = 3
print(first_and_last(nums, target))  # expected: [1, 3]