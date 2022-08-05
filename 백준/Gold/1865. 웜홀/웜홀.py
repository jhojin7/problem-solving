import math

def testcase():
    N,M,W = map(int,input().split())
    edges = []
    pre = [0 for _ in range(N+1)]
    dist = [10001 for _ in range(N+1)]
    # dist[0] = 0
    dist[1] = 0
    
    for _ in range(M):
        u,v,w = map(int,input().split())
        edges.append((u,v,w))
        edges.append((v,u,w))
    for _ in range(W):
        u,v,w = map(int,input().split())
        edges.append((u,v,-w))
    
    for _ in range(N-1):
        for u,v,w in edges:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w
                pre[v] = u

    loop = False
    for u,v,w in edges:
        # if dist update happens, loop=True
        if dist[u]+w < dist[v]:
            dist[v] = dist[u]+w
            loop = True

    if loop: print("YES")
    else: print("NO")

for _ in range(int(input())):
    testcase()