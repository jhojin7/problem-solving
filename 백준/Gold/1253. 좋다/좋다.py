import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
arr = list(map(int,input().split()))
arr.sort()
# S = set([(a,i) for i,a in enumerate(arr)])
S = set(arr)

cnt=0
for i in range(N):
    arrr = arr[:i]+arr[i+1:]
    l,r = 0,len(arrr)-1
    while l<r:
        s = arrr[l]+arrr[r]
        if s==arr[i]:
            cnt+=1
            break
        if s<arr[i]:
            l+=1
        else:
            r-=1
        
print(cnt)