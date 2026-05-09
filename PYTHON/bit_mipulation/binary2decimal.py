str = "1101"
def b2d(str):
    p = 1
    ans = 0
    for char in str[::-1]:
        ans += int(char) * p
        p *= 2
    print(ans)
b2d(str)