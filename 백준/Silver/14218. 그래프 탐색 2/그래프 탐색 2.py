import sys,collections, heapq,math
input=sys.stdin.readline

n,m = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
q = int(input())
dist = [math.inf for _ in range(n+1)]
for _ in range(q):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)
    
    queue = collections.deque([1])
    vis = [-1 for _ in range(n+1)]
    vis[1]=0
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if vis[nxt]!=-1: continue
            queue.append(nxt)
            vis[nxt]=vis[cur]+1
    print(*vis[1:])