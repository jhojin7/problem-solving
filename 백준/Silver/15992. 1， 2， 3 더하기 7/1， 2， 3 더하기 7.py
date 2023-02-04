mod = 10**9+9
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1
for i in range(2,1001):
    for j in range(2,1001):
        dp[i][j] = (dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1])%mod
for _ in range(int(input())):
    n,m = map(int,input().split())
    print(dp[n][m]%mod)