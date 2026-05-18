nums = [2, 7, 11, 15]
target = 9
def twosum():
    frq = dict() 
    for i in range(len(nums)):
         bal = target - nums[i]
         if bal in frq:
            return [i, frq[bal]] 
         frq[nums[i]] = i
print(twosum())