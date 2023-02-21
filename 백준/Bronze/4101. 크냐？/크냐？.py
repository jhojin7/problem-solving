import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

while 1:
    a,b = inputint()
    if (a,b)==(0,0): break
    if a>b: print("Yes")
    else: print("No")
