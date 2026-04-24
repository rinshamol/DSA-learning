# recursion
def fibRecursion(n):
    if(n<=1):
        return n
    return fibRecursion(n-1)+ fibRecursion(n-2)
print(fibRecursion(2))

#memoization
def fibMemoization(n):
    dp = [-1]*(n+1)
    if(n<=1):
        return n
    if(dp[n] != -1):
        return dp[n]
    dp[n] = fibMemoization(n-1) + fibMemoization(n-2)
    return dp[n]

print(fibMemoization(5))

# Tabulation
def fibTabulation(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibTabulation(2))

# optimization
def fibOptimization(n):
    prev = 1
    prev2 = 0
    for i in range(2,n+1):
        curi = prev + prev2
        prev2 = prev
        prev = curi
    return prev
print(fibOptimization(5)) 