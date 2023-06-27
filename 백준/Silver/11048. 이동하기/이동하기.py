import sys; input = sys.stdin.readline
import heapq, collections, itertools

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    dp[i+1][1] = grid[i][0]
for j in range(M):
    dp[1][j+1] = grid[0][j]


for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(
            dp[i-1][j]+grid[i-1][j-1],
            dp[i][j-1]+grid[i-1][j-1],
            dp[i-1][j-1]+grid[i-1][j-1],
        )
print(dp[N][M])