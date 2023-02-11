import sys, collections, heapq, math, re, random
input=sys.stdin.readline
N=int(input())
S = set()
for _ in range(N):
    s = input().strip()
    S.add(s)
for s in S:
    if s in S and s[::-1] in S:
        print(len(s), s[len(s)//2])
        break