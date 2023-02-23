import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

def solve():
    k = int(input())
    words = [inputchars() for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i==j: continue
            new = words[i]+words[j]
            if new==new[::-1]:
                print(new)
                return
    print(0)

for _ in range(int(input())):
    solve()