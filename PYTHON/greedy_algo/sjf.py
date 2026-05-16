A = [4,3,7,1,2]
A.sort()
wt = 0
t = 0
for i in A:
   wt += t
   t += i
avg = wt//len(A)
print(avg)