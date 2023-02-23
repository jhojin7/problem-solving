import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def solvee(): 
    for _ in range(int(input())):solve()
def inputint():return map(int,input().split())
def inputchars():return input().strip()


X = int(input())
arr = [64]
while arr:
    # print(arr)
    if sum(arr)<=X: break
    m = arr.pop(arr.index(min(arr)))
    if m//2+sum(arr)>=X:
        arr.append(m//2)
    else:
        arr.append(m//2)
        arr.append(m//2)

arr.sort(reverse=True)
# print(arr)

ans=0
for a in arr:
    if X<=0: break
    X-=a
    ans+=1
print(ans)