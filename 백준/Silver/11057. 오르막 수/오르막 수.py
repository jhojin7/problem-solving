import sys,collections, heapq,math
input = sys.stdin.readline

N=int(input())
dp = [[0 for _ in range(11)] for _ in range(N+1)]
dp[1] = [1 for _ in range(len(dp[0]))]
dp[1][0]=0
for i in range(1,N): dp[i][1] = 1

for i in range(2,N+1):
    for j in range(1,10):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1])%10007
# print(dp)
print(sum([sum(r) for r in dp])%10007)