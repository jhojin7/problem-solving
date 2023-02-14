import sys, collections, heapq, math, re, random
input=sys.stdin.readline

def solve():
    N=int(input())
    arr = []
    s = set()
    no=False
    for _ in range(N):
        num = input().strip()
        arr.append(num)
        for i in range(len(num)):
            if num in s:
                no=True
                break
            s.add(num[:i])
    for n in arr:
        if n in s:
            no=True
            break
    if no:
        print("NO")
    else:
        print("YES")
    return

for _ in range(int(input())):
    solve()