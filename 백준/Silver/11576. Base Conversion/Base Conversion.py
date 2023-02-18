import sys, collections, heapq, math, re, random
input=sys.stdin.readline

A,B=map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))
ab = 0
for i,a in enumerate(reversed(arr)):
    ab+=a*(A**i)

ans = []
# for i in range(m):
while ab:
    b=ab%B
    ans.append(b)
    ab//=B
print(*reversed(ans),sep=' ')