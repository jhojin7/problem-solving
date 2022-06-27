"""
id: 11725
title:트리의부모찾기
ac:https://www.acmicpc.net/source/45120615
"""
import sys
from io import StringIO
# 8
# 1 6
# 6 3
# 3 5
# 4 5
# 2 4
# 4 7
# 4 8
# 6
# 2 5
# 3 4
# 6 3
# 5 3
# 4 1
sys.stdin = StringIO("""
""".strip())

import sys, collections

N = int(input())
edges_dict = collections.defaultdict(set)
ANSWER = [0 for _ in range(N+1)]

for _ in range(N-1):
    v,w = map(int,input().split())
    edges_dict[v].add(w)
    edges_dict[w].add(v)

def bfs_dict():
    queue = collections.deque([])
    # get edges[1]
    for w in edges_dict[1]: 
        queue.append((1,w))
    # bfs
    visited = set()
    while queue:
        # visit
        parent,child = queue.popleft()
        visited.add(parent)
        # mark parent answer
        if ANSWER[child] != 1 and child not in visited:
            ANSWER[child] = parent
        # append children of child
        for w in edges_dict[child]: 
            if child not in visited:
                queue.append((child,w))

bfs_dict()
for v in range(2,N+1):
    print(ANSWER[v])