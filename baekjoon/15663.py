"""
id: 15663
title:N과M(9)
ac:https://www.acmicpc.net/source/45081467
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
8 8
1 2 3 12 23 34 123 234
""".strip())

import heapq
import sys
def main():
    def dfs(visited:list, visited_i:tuple):
        if len(visited) == M:
            hashed = hash(tuple(visited))
            # hashed = str(visited)
            if hashed not in ans_set:
                ans_set.add(hashed)
                heapq.heappush(ans_heap, visited)
            return
        for i,n in enumerate(arr):
            if i in visited_i: continue
            dfs(visited+[n],visited_i+[i])

    N,M = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split())) 
    ans_set = set()
    ans_heap = []
    dfs([],[])

    while ans_heap:
        l = heapq.heappop(ans_heap)
        for n in l:
            sys.stdout.write(str(n)+' ')
        sys.stdout.write("\n")
main()