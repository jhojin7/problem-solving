import sys,collections, heapq,math
input=sys.stdin.readline

R,C,W = map(int,input().split())
N = R+C+W+1
dp = [[0 for _ in range(N)]
    for _ in range(N)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2,N):
    for j in range(i+1):
        if j==0: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
ans=0
cnt=1
for i in range(R-1,R-1+W):
    for j in range(C-1,C-1+cnt):
        ans+=dp[i][j]
    cnt+=1
print(ans)