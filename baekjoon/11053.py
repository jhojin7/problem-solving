"""
id: 11053
title:가장긴증가하는부분수열
ac:https://www.acmicpc.net/source/44930967
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
6
1 2 1 3 2 5
""".strip())
# 1 2 1 3 2 5

import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
# print(N,arr)

dp = [1] * N 
for i in range(1,N):
    for j in range(0,i):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))