N=int(input())
m = 1000000009
# dp=[[0,0,0] for _ in range(33399)]
dp=[0 for _ in range(33399)]
dp[1] = 0
dp[2] = 2
dp[3] = 6
for i in range(4,N+1):
    dp[i] = dp[i-1]*3%m
print(dp[N])