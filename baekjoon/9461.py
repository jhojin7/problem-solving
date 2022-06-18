"""
id: 9461
title:파도반수열
ac:https://www.acmicpc.net/source/44681461 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
6
12
""".strip())

T = int(input())
dp = [0]*100
dp[:10] = [1,1,1,2,2,3,4,5,7,9]
for _ in range(T):
    N = int(input())
    for i in range(5,N):
        dp[i] = dp[i-1] + dp[i-5]
    # print(dp)
    print(dp[N-1])