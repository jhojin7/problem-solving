import collections

def bfs(src,dest):
    queue = collections.deque([(src,0)])
    visited = set()
    while queue:
        u,w = queue.popleft()
        if u == dest: return w
        if u in visited: continue
        visited.add(u)
        for v,ww in graph[u]:
            if v not in visited:
                queue.append((v,w+ww))

N,M = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(N-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
for _ in range(M):
    u,v = map(int,input().split())
    print(bfs(u,v))