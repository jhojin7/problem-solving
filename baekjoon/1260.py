"""
dfs와bfs
https://www.acmicpc.net/source/44399814
with bisect.insort: https://www.acmicpc.net/source/44400346
"""
import sys
from io import StringIO
# 1000 1 1000
# 999 1000
testcases = """
4 5 1
1 2
1 3
1 4
2 4
3 4
""".strip()
# https://stackoverflow.com/a/5062926/3413574
# https://stackoverflow.com/a/34168892/3413574
sys.stdin = StringIO(testcases)
###############################################

import bisect
import collections
def dfs(node, _visited:list):
    # visit
    _visited.append(node)
    # do dfs
    for n in edges[node]:
        if n not in _visited:
            dfs(n,_visited)

def bfs(start, _visited:list):
    # visit first node
    _visited.append(start)
    # check all possible edges
    queue = collections.deque(edges[start])
    # do bfs
    while queue:
        node = queue.popleft()
        # visit
        if node not in visited:
            _visited.append(node)
        # add node's vertices
        for n in edges[node]:
            if n not in visited:
                queue.append(n)
        # if all nodes are visited, exit
        if set(visited) == set(edges.keys()):
            return
    return

N, M, start= map(int,input().split())
edges = collections.defaultdict(list)
for _ in range(M):
    src, dest = map(int,input().split())
    bisect.insort(edges[src],dest)
    bisect.insort(edges[dest],src)
    # edges[src].append(dest)
    # edges[dest].append(src)

# # sort for traversal order
# for n in range(M):
#     edges[n].sort()

visited = []
dfs(start, visited)
print(*visited,sep=' ')

visited = []
bfs(start, visited)
print(*visited,sep=' ')