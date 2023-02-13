import sys, collections, heapq, math, re, random
input=sys.stdin.readline

nums = [False for _ in range(1001)]
nums[1] = True
for i in range(2,1001):
    if nums[i]: continue
    for j in range(i*2,1001,i):
        nums[j]=True

def solve():
    ok=False
    K = int(input())
    for a in range(2,1001):
        if nums[a]: continue
        for b in range(2,1001):
            if nums[b]: continue
            for c in range(2,1001):
                if nums[c]: continue
                if a+b+c==K:
                    print(a,b,c)
                    ok=True
                    break
            if ok: break
        if ok: break
    if not ok: print(0)

for _ in range(int(input())):
    solve()