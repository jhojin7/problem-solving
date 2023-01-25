import sys,collections, heapq,math
input=sys.stdin.readline

global aa
global bb
aa,bb=0,0
def b(n):
    global bb
    dp=[0 for _ in range(100)]
    dp[0]=1
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        bb+=1
    return dp[n]
def a(n):
    global aa
    if n==1 or n==2:
        aa+=1
        return 1
    return a(n-1)+a(n-2)

n=int(input())
a(n)
b(n)
print(aa,bb)