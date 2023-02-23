import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
d = collections.defaultdict(int)
for _ in range(N):
    x,y = inputchars().split('.')
    d[y]+=1
# print(d)
for k in sorted(d.keys()):
    print(k,d[k])