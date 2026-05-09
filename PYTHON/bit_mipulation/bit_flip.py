A = 7
def solve( A):
        l = A.bit_length()
        mask = (1 << l) -1
        r = A ^ mask
        return r
print(solve(A))