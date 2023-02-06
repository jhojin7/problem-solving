N=int(input())
dp = [0 for _ in range(N+1)]
dp[:2] = [0,1,2]
for i in range(3,N+1):
    dp[i] = (dp[i-1]+dp[i-2])%15746
# print(dp)
print(dp[N]%15746)