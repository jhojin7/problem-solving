import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N = int(input())
arr = [99999]+list(map(int,input().split()))

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        for i in range(b,N+1,b):
            arr[i] = 0 if arr[i]==1 else 1
    elif a==2:
        l,r = b,b
        while 0<=l<=N and 0<=r<=N:
            if arr[l]!=arr[r]:
                break
            if l==r:
                arr[l] = 0 if arr[l]==1 else 1
            else:
                arr[l] = 0 if arr[l]==1 else 1
                arr[r] = 0 if arr[r]==1 else 1
            l-=1
            r+=1
# arr = [99 for _ in range(22)]
if len(arr)<=20:
    print(*arr[1:])
else:
    arr = arr[1:]
    for i in range(len(arr)):
        print(arr[i],end=' ')
        if (i+1)%20==0: print()