A = [1,2,3]
def sum_bit():
    res = []
    for i in range(len(arr)):
        xor = arr[i]
        res.append(arr[i])
        for j in range(i+1,len(arr)):
            xor ^= arr[j]
            res.append(xor)
    
# sum_bit()
def solve():
        xor = A[0] ^ A[len(A)-1]
        
        print(xor)
solve()