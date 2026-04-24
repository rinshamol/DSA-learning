n = int(input())
num = 1
i = n//2
j = n - 1
magic_square = [[0]*n for _ in range(n)]
magic_square[i][j] = num
while num < n*n :
    
    i = (i-1) % n
    j = (j+1) % n
    if( magic_square[i][j] == 0):
        num += 1
        magic_square[i][j] = num
    else :
        i = (i + 1) % n
        j = (j - 2) % n
    
    if(i == -1 and j == n) :
        i = 0
        j = n-2

for r in magic_square :
    print(r)
