import sys, collections, heapq, math, re, random
input=sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    x,y = min(x,y),max(x,y)
    arr.append((x,y))
arr.sort()
ans=0
l,r=arr[0]
for x,y in arr:
    if r<x:
        ans+=(r-l)
        l,r = x,y
    else:
        r=max(r,y)
ans+=(r-l)
print(ans)