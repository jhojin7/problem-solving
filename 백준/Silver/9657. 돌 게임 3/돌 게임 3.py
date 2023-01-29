import sys, collections, heapq, math, re

N = int(input())
sk="SK"
cy="CY"
dp = ['' for _ in range(N+1)]
dp[:6] = ['',sk,cy,sk,sk,sk]
for i in range(6,N+1):
    dp[i]=cy
    if dp[i-1]==cy: dp[i]=sk
    if dp[i-3]==cy: dp[i]=sk
    if dp[i-4]==cy: dp[i]=sk
print(dp[N])