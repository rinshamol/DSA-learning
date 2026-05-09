# arr = [726354, 112938, 984756, 345210, 667788, 123456, 999999, 888888, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1, 876543, 234567, 456789, 678901, 890123, 101112, 131415, 161718, 192021, 222324, 252627, 282930, 313233, 343536, 373839, 404142, 434445, 464748, 495051, 525354, 555657, 585960, 616263, 646566, 676869, 707172, 737475, 767778, 798081, 828384, 858687, 888990, 919293, 949596, 979899, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090, 121212, 232323, 343434, 454545, 565656, 676767, 787878, 898989, 909091, 123123, 234234, 345345, 456456, 567567, 678678, 789789, 890890, 901901, 121314, 151617, 181920, 212223, 242526, 272829, 303132, 333435, 363738, 394041, 424344, 454647, 484950, 515253, 545556, 575859, 606162, 636465, 666768, 697071, 727374, 757677, 787980, 818283, 848586, 878889, 444111, 555222]
arr = [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
n = len(arr)
maxi = [0]
# level 1
def max_xor(dp,ind):
    if len(dp) > n:    
        return 0
    xor = 0
    for i in dp:
        xor = xor ^ i
    maxi[0] = max(maxi[0], xor)
    for i in range(ind,len(arr)):
        dp.append(arr[i])
        l = max_xor(dp,i + 1)
        maxi[0] = max(maxi[0],l)
        dp.pop()
    return xor
# max_xor([],0)
# print(maxi[0])
# optimal solution using bitmasking and bucket concept/ linear basis
def solve():
    
    
    max_elements = n // 2
    max_xor = 0
    
    # ===== For small N: Brute Force with Bitmask =====
    if n <= 20:
        # Try all possible subsets using bitmask
        for mask in range(1 << n):  # 2^n possibilities
            # Count number of set bits in mask
            if bin(mask).count('1') > max_elements:
                continue  # Skip if we have more than n//2 elements
            
            # Calculate XOR of elements in this subset
            xor_val = 0
            for i in range(n):
                if mask & (1 << i):  # If i-th bit is set
                    xor_val ^= arr[i]
            
            max_xor = max(max_xor, xor_val)
        
        return max_xor
    
    # ===== For large N: Linear Basis (N > 20) =====
    basis = [0] * 30  # One slot per bit (covers up to 2^30 ≈ 10^9)
    
    # Build the basis
    for num in arr:
        cur = num
        for bit in range(29, -1, -1):
            # Check if this bit is set in cur
            if not (cur & (1 << bit)):
                continue
            
            # If we don't have a basis element for this bit, add it
            if basis[bit] == 0:
                basis[bit] = cur
                break
            
            # Otherwise, XOR with existing basis element to cancel this bit
            cur ^= basis[bit]
    
    # Greedily maximize XOR
    result = 0
    for bit in range(29, -1, -1):
        if basis[bit] != 0:
            # Try XORing with this basis element
            if (result ^ basis[bit]) > result:
                result ^= basis[bit]
    
    return result

print(solve())