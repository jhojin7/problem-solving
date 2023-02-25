import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
arr = []
for _ in range(N):
    name,dd,mm,yyyy = input().split()
    arr.append((int(yyyy),int(mm),int(dd),name))
arr.sort()
print(arr[-1][-1])
print(arr[0][-1])

