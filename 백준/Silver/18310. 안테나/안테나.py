import sys, collections, heapq, math, re
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
arr.sort()
# print(arr)
if len(arr)<=1:
    print(arr[0])
    exit()

m=len(arr)//2
x,y=arr[m-1],arr[m]
# print(x,y)
xx,yy=0,0
for n in arr:
    xx+=abs(n-x)
    yy+=abs(n-y)
# print(xx,yy)
if xx<=yy: print(x)
else: print(y)