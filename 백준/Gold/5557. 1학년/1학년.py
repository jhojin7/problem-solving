import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
arr = list(inputint())
dp = [[0 for _ in range(22)] for _ in range(N+1)]
dp[0][arr[0]] = 1
for i in range(len(arr)):
    for j in range(21):
        a = j+arr[i]
        b = j-arr[i]
        if 0<=a<=20: dp[i][a]+=dp[i-1][j]
        if 0<=b<=20: dp[i][b]+=dp[i-1][j]
print(dp[N-2][arr[-1]])
# print(dp)


