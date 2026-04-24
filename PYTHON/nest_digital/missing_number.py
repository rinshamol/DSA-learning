
def missingNumber( nums) -> int:
        i = 0
        n = len(nums)
        while i < n:
            correct = nums[i]
            if(nums[i] < n and nums[i] != nums[correct]):
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i += 1
        for i,num in enumerate(nums):
            if(num != i):
                return i
        return n
nums = [3,0,1]
print(missingNumber(nums))