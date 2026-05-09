# max xor from arr constrain N/2
# for input size <=20
def max_xor():
    max_xor = 0
    arr = [3,4,7,1,1,1,1,1,1000]
    m = len(arr)
    n = len(arr) // 2
    for mask in range(1<< m):
        if bin(mask).count('1') > n:
            continue
        xor = 0
        for i in range(m):
            if mask & 1 << i:
                xor ^= arr[i]
        max_xor = max(max_xor,xor)
    return max_xor
print(max_xor())