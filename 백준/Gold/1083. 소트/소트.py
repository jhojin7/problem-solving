import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N=int(input())
A = list(map(int,input().split()))
S=int(input())

for k in range(N):
    if S==0: break
    maxval = max(A[k:k+S+1])
    maxidx = A.index(maxval)
    for i in range(maxidx-1,-1,-1):
        if S==0: break
        if A[i]<A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
            S-=1
    # print(S)
print(*A)