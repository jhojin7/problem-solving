import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
T=list(map(int,input().split()))

T.sort(reverse=True)
aa=0
for i,t in enumerate(T,2):
    a = i+t
    aa = max(a,aa)
print(aa)