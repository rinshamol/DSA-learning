A=3
res = []
def solve(A): 
    nums = list(range(1,A+1))
    permutation(0,nums,res)
    print(res)
    return sum(res)

def permutation( ind, nums,res):
    if ind == len(nums):
        cost = 0
        for n in range(1,ind):
            if nums[0] > nums[n]:
                cost += nums[n]
        res.append(cost)
        return
    
    for i in range(ind,len(nums)):
        nums[ind],nums[i] = nums[i],nums[ind]
        permutation(ind + 1, nums,res)
        nums[ind],nums[i] = nums[i],nums[ind]
print(solve(A))