import sys; input = sys.stdin.readline
import heapq, collections, itertools


arr = [ input().strip() for _ in range(int(input()))]
cnter = collections.Counter(arr).items()
cnter = sorted(cnter, key=lambda x: -x[1])
ans = []
ans.append(cnter[0][0])
for k,v in cnter[1:]:
    if v==cnter[0][1]:
        ans.append(k)

print(*sorted(ans),sep='\n')