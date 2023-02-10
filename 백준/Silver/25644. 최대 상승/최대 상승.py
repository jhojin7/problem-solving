import sys, collections, heapq, math, re
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))

m = math.inf
ans = 0
for i,x in enumerate(arr):
    ans = max(ans, x-m)
    m = min(m,x)
print(ans)