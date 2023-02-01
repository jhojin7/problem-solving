import sys, collections, heapq, math, re
# sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# N=int(input())

N=500002
arr=[True for _ in range(N)]
arr[0]=False
arr[1]=False

for i in range(2,N):
    if arr[i]==False:
        continue
    for j in range(i*2,N,i):
        arr[j]=False
k=int(input())
# print(arr[:k])
cnt=0
for i in range(N):
    if arr[i]: cnt+=1
    if cnt==k:
        print(i)
        break
    