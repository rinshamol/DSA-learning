def containsDuplicate(nums) -> bool:
        return len(set(nums)) != len(nums)
        # seen = {}
        # for i,num in enumerate(nums):
        #     if(num in seen):
        #         return True
        #     else:
        #         seen[num] = 1
        # return False
nums = [1,2,3,1]
print(containsDuplicate(nums))