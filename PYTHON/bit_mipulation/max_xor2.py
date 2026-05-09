# for input size > 20
def max_xor():
    arr = [5,3,7,4]
    n = len(arr)
    
    basis = [0]*30
    for num  in arr:
        cur = num
        for bit in range(29,-1,-1):
            if not cur &(1<<bit):
                continue
            if basis[bit] == 0:
                basis[bit] = cur
                break
            cur ^= basis[bit]
    result = 0
    for bit in range(29,-1,-1):
        if result^basis[bit] > result:
            result ^= basis[bit]
    print(result)
max_xor() 