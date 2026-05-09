nums = [1,2,3]
res = []
n = 3
def swap(a,b):
    a,b = b,a
def permutation(ind):
    if ind ==  n:
        res.append(nums)
        return
    for i in range(ind,n):
        swap(nums[ind],nums[i])
        permutation(ind + 1)
        swap(nums[ind],nums[i])
permutation(0)
print(len(res))

print(res)