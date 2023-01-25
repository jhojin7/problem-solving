def solution(triangle):
    N=len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = triangle[0][0]
    for i in range(1,N):
        for j in range(i+1):
            if j==0: 
                dp[i][j]=triangle[i][j] + dp[i-1][j]
            else: 
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j])
    return max(dp[-1])
