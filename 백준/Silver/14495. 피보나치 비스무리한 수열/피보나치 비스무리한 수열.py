import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N = int(input())
dp = [0 for _ in range(1000)]
dp[1]=dp[2]=dp[3]=1
for i in range(4,1000):
    dp[i] = dp[i-1]+dp[i-3]
print(dp[N])