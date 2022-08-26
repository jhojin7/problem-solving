n,r = map(int, input().split())
dp = [[0 for _ in range(33)] for _ in range(33)]
for i in range(1,n+1):
    dp[i][1]=1
    dp[i][i]=1
for i in range(2,n+1):
    for j in range(2,i):
        dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
print(dp[n][r])