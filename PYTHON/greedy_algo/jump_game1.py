A = [1,2,3,1,1,0,2,5]
def jump_game():
    
    max_jump = 0
    n = len(A)
    if not 0 in A:
        return True
    for i in range(n):
        if max_jump < i:
            return False
        max_jump = max(max_jump, i+ A[i])
        
    return True
print(jump_game())