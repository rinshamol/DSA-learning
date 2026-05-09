start = 13
goal = 7
count = 0
ans = start ^ goal
for i in range(32):
    if (ans & (1 << i)):
        count += 1
print(count)