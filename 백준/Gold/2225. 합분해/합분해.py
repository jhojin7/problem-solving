mod = 10**9
N,K = map(int,input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]
dp[1] = [k for k in range(201)] 
for i in range(201): dp[i][1]=1
for i in range(2,N+1):
    for j in range(2,K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod
print(dp[N][K]%mod)
