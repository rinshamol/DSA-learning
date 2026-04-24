def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int(start +(end - start)/2)
        if(nums[mid] == target):
            return mid
        if(nums[mid]> target):
            end = mid - 1
           
        else:
            start = mid + 1
    return -1
nums = [1, 2, 3, 4, 5]
target = 3
print(binarySearch(nums,target))