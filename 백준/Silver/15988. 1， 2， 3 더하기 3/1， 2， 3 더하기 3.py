import sys, collections, heapq, math, re
input=sys.stdin.readline
# sys.setrecursionlimit(10**5)
# N=int(input())
m=10**6+1
mod = 10**9+9
dp=[0 for _ in range(m)]
dp[:5]=[0,1,2,4,7]
for i in range(5,m):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%mod
for _ in range(int(input())):
    print(dp[int(input())]%mod)