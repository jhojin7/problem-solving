n=int(input())
dp = [0 for _ in range(100)]
dp[0]=1
dp[1]=1
for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]
ans = dp[n-1]*2+(dp[n-1]+dp[n-2])*2
print(ans)