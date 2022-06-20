"""
id: 1932
title:정수삼각형
ac: 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
""".strip())

N = int(input())
triangle = []
for _ in range(N):
    row = map(int,input().split())
    triangle.append([*row])

dp = []
for _ in range(N+1):
    dp.append([0]*(N+1)) # 이상하게 초기화하는거 주의..
print(N,triangle)

#  table
for i in range(1,N+1):
    for j in range(1,i+1):
        # cur = dp[i][j]
        cur = triangle[i-1][j-1]
        prev_left = dp[i-1][j-1]
        prev_right = dp[i-1][j]
        dp[i][j] = max(cur+prev_left, cur+prev_right)
        print(i,j, dp[i][j])
    print(dp)
print(max(dp[-1]))