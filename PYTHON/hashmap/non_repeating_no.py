# Given a list of numbers, return the first non-repeating number.
nums = [4, 5, 4, 6, 5, 7]
# answer = 6

def non_rep_no(nums):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i,0) + 1
    for u,v in freq.items():
        if v == 1:
            return u
    return  -1
print(non_rep_no(nums))