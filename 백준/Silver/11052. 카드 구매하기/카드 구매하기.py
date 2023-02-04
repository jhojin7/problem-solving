N=int(input())
P = [0] + list(map(int,input().split()))
nn = N
dp = [0 for _ in range(N+1)]
dp[1] = P[1]
dp[2] = max(P[2],2*P[1])
for i in range(3,N+1):
    tmp = []
    for x in range(1,i):
        tmp.append(dp[i-x]+dp[x])
    dp[i] = max(
        dp[i-1]+P[1],P[i],P[i//2]*2,
        max(tmp)
    )
print(dp[N])