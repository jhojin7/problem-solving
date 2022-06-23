"""
id: 2150
title: strongly connected component
ac:https://www.acmicpc.net/source/44930562
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

# scc tarjan implementation
import sys, collections
# RecursionError
sys.setrecursionlimit(10**5) #백준

V, E = map(int,input().split())
if not (1 <= V <= 10000 and 1 <= E <= 100000):
    exit(-1)
graph = collections.defaultdict(list)
lowlink = [0] * (V+1)
index = [-1] * (V+1) # -1 = undefined
idx = 0
stack = collections.deque([])
SCCs = []

for _ in range(E):
    v,w = map(int,input().split())
    graph[v].append(w)

def strongconnect(v):
    global idx
    index[v] = idx
    lowlink[v] = idx
    idx += 1
    stack.append(v)

    for w in graph[v]:
        if index[w] == -1:
            strongconnect(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in stack:
            lowlink[v] = min(lowlink[v], index[w])
    
    if lowlink[v] == index[v]:
        scc = []
        while stack:
            w = stack.pop()
            scc.append(w)
            if w == v: break
        SCCs.append(sorted(scc))

for v in range(1,V+1):
    if index[v] == -1:
        strongconnect(v)

# print(stack)
print(len(SCCs))
for scc in sorted(SCCs):
    print(*scc,sep=' ',end=' -1\n')