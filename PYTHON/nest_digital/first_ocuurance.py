def findFirstOccurrence(nums, target):
    start =  0
    end = len(nums)-1
    ans = -1
    while(start <= end):
        mid = start + (end- start)//2
        if(nums[mid] == target):
            ans = mid
            end = mid - 1
            
            
        elif(nums[mid] > target):
            end = mid -1
        else:
            start = mid + 1
    return ans
nums = [1, 2, 3, 4, 5]
target = 3
print(findFirstOccurrence(nums,target))