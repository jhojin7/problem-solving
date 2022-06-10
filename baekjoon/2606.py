"""
problem: https://www.acmicpc.net/problem/2606
ac: https://www.acmicpc.net/source/44402281
"""
import sys
from io import StringIO
testcases = """
7
6
1 2
2 3
1 5
5 2
5 6
4 7
""".strip()
sys.stdin = StringIO(testcases)
###############################################
import collections
import bisect
def bfs(start, _visited:list):
    # visit first node
    _visited.append(start)
    # check all possible edges
    queue = collections.deque(edges[start])
    # do bfs
    while queue:
        node = queue.popleft()
        # visit
        if node not in _visited:
            _visited.append(node)
        # add node's vertices
        for n in edges[node]:
            if n not in _visited:
                queue.append(n)
        # if all nodes are visited, exit
        if set(_visited) == set(edges.keys()):
            return
    return

comp_cnt = int(input())
edges_cnt = int(input())
edges = collections.defaultdict(list)
for _ in range(edges_cnt):
    src, dest = map(int,input().split())
    bisect.insort(edges[src],dest)
    bisect.insort(edges[dest],src)

visited = []
bfs(1, visited)
print(len(visited)-1) # dont include start point