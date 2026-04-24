nums = list(map(int,input().split()))
# //optimized kadane's algo
def maximumSum(nums):
    max = float('-inf')
    sum = 0
    for i in range (0,len(nums)):
        sum += nums[i]
        # if( sum < 0):
        #     sum = 0
        if(sum > max):
            max = sum
    return max

print("MaxSum:", maximumSum(nums))