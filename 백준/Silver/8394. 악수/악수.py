n=int(input())
dp = [0 for _ in range(n+1)]
dp[1]=1
dp[2]=2
# dp[3]=3
# 5...
for i in range(3,n+1):
    dp[i] = (dp[i-2]+dp[i-1])%10
print(dp[n])