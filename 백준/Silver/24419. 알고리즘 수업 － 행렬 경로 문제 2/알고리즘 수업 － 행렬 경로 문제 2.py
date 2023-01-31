N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
mod = 10**9+7

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0] = [1 for _ in range(N)]
for i in range(N): dp[i][0]=1
ans=N*2

for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod
        ans=(ans+dp[i][j])%mod
print(ans%mod,N*N)