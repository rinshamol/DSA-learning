health = [10,20,30,10]
n= len(health)+1
# memoization
dp = [-1]*n
def frog_jump(index):
	
	if(index == 0):
		return 0
	if(dp[index] != -1):
		return dp[index]
	left = frog_jump(index-1) + abs(health[index]-health[index-1])
	right = float('inf')
	if(index > 1):
		right = frog_jump(index-2) + abs(health[index] - health[index - 2])
	dp[index] = min(left,right)
	return dp[index]

print(frog_jump(len(health)-1))

# Tabulation
def frog_jump_tb(index):
	dp[0] = 0
	for index in range(1,n-1):
	
		left = dp[index-1] + abs(health[index] - health[index-1])
		right = float('inf')
		if(index > 1):
			right = dp[index-2] + abs(health[index]- health[index - 2])
		dp[index] = min(left,right)
	return dp[index]

print(frog_jump_tb(len(health)-1))

# Space Optimised
def frog_jump_so(index):
	prev = 0
	prev2 = 0
	for i in range(1,index):
		left = prev + abs(health[i]-health[i-1])
		right = float('inf')
		if(i > 1):
			right = prev2 + abs(health[i]-health[i-2])
		cur = min(left,right)
		prev2 = prev
		prev = cur

	return prev
print(frog_jump_so(len(health)-1))
