import collections
N=int(input())
graph = collections.defaultdict(list)
edges = []
for _ in range(N-1):
    u,v = map(int,input().split())
    edges.append((u,v))
    graph[u].append(v)
    graph[v].append(u)

q = int(input())
for _ in range(q):
    t,k = map(int,input().split())
    # check if k is leaf
    isleaf = False
    if len(graph[k])==1: isleaf=True
    # print(graph[k])
    if t==1:
        if isleaf: print("no")
        else: print("yes")
    elif t==2:
        # a,b = edges[k]
        print("yes")