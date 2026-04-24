greed = [1,5,3,3,4]
cookies = [4,2,1,2,1,3]
greed.sort()    #[1,3,3,4,5]
cookies.sort()  #[1,1,2,2,3,4]
g = 0
n = len(greed)-1
c = 0
m = len(cookies)-1
while c < m:
    if greed[g] <= cookies[c]:
        g += 1
    c += 1
print(g + 1)
