from collections import defaultdict
nums = [1,2,3]
n = 3
res = []
freq = defaultdict(bool)
ds = []
def recursive_permu(freq,ds):
    if len(ds) == n:
        res.append(ds)
        return
    for i in range(n):
        if freq[i] == False:
            freq[i] = True
            ds.append(nums[i])
            recursive_permu(freq,ds)
            ds.pop()
            freq[i] = False
recursive_permu(freq,ds)
print(len(res))