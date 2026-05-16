A = [2, 3, 1, 1, 4]
def jump_game():
    maxi = 0
    max_jump = 0
    count = 0
    n = len(A)
    for i in range(n):
        maxi = i + A[i]
        if max_jump < maxi :
            count += 1
            max_jump = maxi
            if max_jump >= n-1:
                break
        
    print(count)
jump_game()
# striver method
def method2():
    jumps = 0
    l = 0
    r = 0
    n = len(A)
    while(r < n-1):
        farthest = 0
        for i in range(l,r+1):
            farthest = max(i + A[i],farthest)
        l = r+1
        r = farthest
        jumps += 1
    print(jumps)
method2()