import sys, collections, heapq, math, re, random
input=sys.stdin.readline

globalans = []
def solve():
    s = input().strip()
    arr = []
    for c in s:
        if c in "1234567890":
            arr.append(c)
        else:
            arr.append(' ')
    arr = list(map(int,''.join(arr).split()))
    globalans.extend(arr)
for _ in range(int(input())):
    solve()
print(*sorted(globalans),sep='\n')