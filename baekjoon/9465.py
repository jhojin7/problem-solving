"""
id: 9465
ac:https://www.acmicpc.net/source/45653035
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
""".strip())

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0]+list(map(int,input().split())) for _ in range(2)]
    # print(n,dp)
    
    for j in range(2,n+1):
        # dp[0][j] += min(dp[1][j-1],dp[1][j-1]+dp[0][j])
        dp[0][j] += max(dp[1][j-1],dp[1][j-2])
        dp[1][j] += max(dp[0][j-1],dp[0][j-2])
    # print(*dp,sep='\n')
    a,b = (dp[0][-1], dp[1][-1])
    # print(a,b)
    print(a if a>b else b)
