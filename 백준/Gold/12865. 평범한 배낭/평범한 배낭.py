N,K = map(int,input().split())
stuff = []
for _ in range(N):
    w,v = map(int,input().split())
    stuff.append((w,v))
stuff.sort(reverse=True)

dp = [[0 for _ in range(K+1)] 
        for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        weight,value = stuff[i-1]
        if weight<=j:
            dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])