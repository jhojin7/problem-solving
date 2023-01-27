import sys,collections, heapq,math
input = sys.stdin.readline

N=int(input())
for _ in range(N):
    s=list(input().split())
    x=float(s.pop(0))
    while s:
        op = s.pop(0)
        if op=='@': x*=3
        elif op=='%': x+=5
        elif op=='#': x-=7
    print(f"{x:.2f}")