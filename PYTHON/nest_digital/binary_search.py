def search(nums, target) -> int:
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = int(start + (end - start)/2)
        if(nums[mid] == target):
            return mid
        if(nums[mid] < target):
            start = mid+1
        else:
            end = mid -1

    return -1
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))