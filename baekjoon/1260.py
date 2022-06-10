"""
dfs와bfs
https://www.acmicpc.net/source/44399814
"""
import sys
from io import StringIO
testcases = """
1000 1 1000
999 1000
""".strip()
# https://stackoverflow.com/a/5062926/3413574
# https://stackoverflow.com/a/34168892/3413574
sys.stdin = StringIO(testcases)
###############################################

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
    edges[src].append(dest)
    edges[dest].append(src)

# sort for traversal order
for n in range(M):
    edges[n].sort()

visited = []
dfs(start, visited)
print(*visited,sep=' ')

visited = []
bfs(start, visited)
print(*visited,sep=' ')