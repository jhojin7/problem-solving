import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()


D,K = map(int,input().split())

def solve(A,B):
    arr = [A,B]
    while len(arr)<D:
        arr.append(arr[-1]+arr[-2])
        if arr[-1]>K:
            return False
    if arr[-1]==K:
        # print(arr)
        return True
    else: return False

for A in range(1,K):
    for B in range(A,K):
        if solve(A,B):
            print(A)
            print(B)
            exit()
