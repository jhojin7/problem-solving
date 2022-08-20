N=int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
mod = 1000000000
if N==1: 
    print(9)
    exit()
for j in range(1,10):
    dp[1][j] = 1
for i in range(2,N+1):
    for j in range(10):
        if j==0:
            dp[i][j] = (dp[i-1][j+1])%mod
        elif j==9:
            dp[i][j] = (dp[i-1][j-1])%mod
        else:
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%mod
print(sum(dp[N])%mod)
# print(dp)