import sys,collections, heapq,math
input=sys.stdin.readline
dp=[0 for _ in range(1001)]
dp[1]=1
dp[2]=3
for i in range(2,1001):
    dp[i]=dp[i-1]+i

for i in range(1,int(input())+1):
    n=int(input())
    ans=sum(dp[:n+1])
    print(f"{i}: {n} {ans}")