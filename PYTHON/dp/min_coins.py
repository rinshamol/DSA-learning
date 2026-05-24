# Given a list of coins and a target amount, find the minimum number of coins needed to make that amount. You can use each coin unlimited times.
coins = [1, 3, 4]
amount = 10
# answer = 2 (3+3)   

def min_coins(coins, amount):
    dp = {}
    dp[0] = 0
    for i in range(amount + 1):
        for c in coins:
            if c <= i:
                take =  dp[i - c] + 1
                dp[i] = min(dp.get(i,float('inf')),take)
    return dp[amount]
    
print(min_coins(coins,amount))