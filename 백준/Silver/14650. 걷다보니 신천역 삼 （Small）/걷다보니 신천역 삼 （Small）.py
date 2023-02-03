N=int(input())
dp=[0 for _ in range(N+1)]
dp[:4]=[0,0,2,6]#18
for i in range(4,N+1):
    dp[i] = dp[i-1]*3 
print(dp[N])