def findLongestArithmeticProgression(arr, k):
    s = set(arr)
    max_len = 0
    for a in arr:
        if a - k not in s:
            current = a
            length = 1
            while current + k  in s:
                current += k
                length += 1
            max_len = max(max_len, length)
    return max_len
arr = [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9]
k = 2
print(findLongestArithmeticProgression(arr,k))