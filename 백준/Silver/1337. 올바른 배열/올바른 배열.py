import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

arr = [int(input()) for _ in range(int(input()))]
arr.sort()
# print(arr)
maxcnt=0

for i in range(len(arr)):
    x = arr[i]
    # print(arr[i:i+5])
    ans = set([x])
    for y in [x+1,x+2,x+3,x+4]:
        if y in arr[i+1:i+5]:
            ans.add(y)
    # print(ans)
    maxcnt = max(maxcnt,len(ans))
print(5-maxcnt)