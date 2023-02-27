import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

def solve():
    N=int(input())
    coin = [11111]+list(map(int,input().split()))
    M=int(input())
    # dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp = [0 for _ in range(M+1)]

    dp[0]=1
    for i in range(1,N+1):
        # print(coin[i])
        # dp[i][coin[i]]=1
        for j in range(coin[i],M+1):
            # print(" ",j,j-coin[i])
            dp[j] += dp[j-coin[i]]
    print(dp[M])

for _ in range(int(input())):
    solve()