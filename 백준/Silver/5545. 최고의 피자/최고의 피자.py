import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline

N=int(input())
A,B = map(int,input().split())
C=int(input())
D = [int(input()) for _ in range(N)]
D.sort(reverse=True)
cal = C
price = A
ans = cal/price

for i,d in enumerate(D,1):
    cal+=d
    price+=B
    # print(i,d,cal,cal/price)
    ans = max(ans,cal/price)

print(math.floor(ans))