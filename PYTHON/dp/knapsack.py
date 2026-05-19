def knapsack(weight, values, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(0,W+1):
            if weight[i-1] > w :
                dp[i][w] = dp[i-1][w]
            else:
                skip = dp[i-1][w]
                take  = values[i-1] + dp[i-1][w - weight[i-1]]
                dp[i][w] = max(skip,take)
    return dp[n][W]
weights = [1, 2, 3]
values  = [6, 10, 12]
W = 5
print(knapsack(weights, values, W))  # expected: 22