def rob(houses):
    dp = {0: houses[0], 1: max(houses[0], houses[1])}
    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])
    return dp[len(houses)-1]
houses = [2, 7, 9, 3, 1]
print(rob(houses))  # should print 12