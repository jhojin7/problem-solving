"""
id: 11724
title:연결요소의개수
ac:https://www.acmicpc.net/source/44775047
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
6 2
3 4
4 2
""".strip())

def dfs(node,component):
    # visit
    g_visited.append(node)
    # save node to current component
    component.append(node)
    # print(node, component,g_visited)
    for u,v in edges:
        if u == node and v not in component: 
            dfs(v,component)

import sys
N, M = map(int,sys.stdin.readline().split())
edges = []
for _ in range(M):
    u,v = tuple(map(int,sys.stdin.readline().split()))
    edges.append((u,v))
    edges.append((v,u)) # undireced graph. use both ways
# print(N,M,edges)

# global visited
g_visited = []
# all components
all_components = []
# traverse all nodes
for u in range(1,N+1):
    # if not visited, do dfs 
    if u not in g_visited:
        component = []
        dfs(u,component)
        all_components.append(component)
        # print(">",u,g_visited)
# return count of components
print(len(all_components))
# print(all_components)