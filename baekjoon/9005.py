"""
id: 9095
title: 123더하기
ac: https://www.acmicpc.net/source/44671254
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3
4
7
10
""".strip())

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * 11 # 1,2,4,7,...
    dp[1] = 1# 1->1
    dp[2] = 2# 2->1+1,//2
    dp[3] = 4# 3->1+1+1,1+2,//2+1,3
    dp[4] = 7# 4->1+1+1+1,1+1+2,1+2+1,1+3//2+1+1,2+2,3+1
    # 5->1+1+1+1+1,1+1+1+2,1+1+2+1,1+1+3//1211,122,131//2111,311,212,221,...
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])