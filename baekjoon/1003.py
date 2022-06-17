"""
title: 1003 피보나치함수
ac: https://www.acmicpc.net/source/44663638
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3
0
1
3
""".strip())

T = int(input())
for _ in range(T):
    N = int(input())
    # if N == 0, 1
    if N == 1:
        print("0 1")
        continue
    if N == 0:
        print("1 0")
        continue
    # fibonacci dp
    dp = [0]*(N+1)
    dp[0], dp[1] = 1,1
    for n in range(2,N+1):
        dp[n] = dp[n-1] + dp[n-2]
    print(dp[-3], dp[-2])