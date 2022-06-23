"""
id: 11600
title:구간합구하기5
ac:https://www.acmicpc.net/source/44886829
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
""".strip())
# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4

# input
import sys
N, M = map(int,sys.stdin.readline().split())
dp = [[0 for _ in range(N+1)]]
for i in range(N):
    dp.append([0] + list(map(int,sys.stdin.readline().split())))
# print(*dp,sep='\n')
# prefix sum
# dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        # dp = self + [i-1] + [j-1] - [i-1][j-1]
        dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
# print(*dp,sep='\n')
# do calculation
for i in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(ans)