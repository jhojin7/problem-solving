import sys,collections
input = sys.stdin.readline
N,M = map(int,input().split())
graph = collections.defaultdict(set)
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].add(v)
    graph[v].add(u)

def bfs(src,dest):
    dist = 0
    queue = collections.deque([(src,0)])
    visited = set()
    while queue:
        u,dist = queue.popleft()
        if u in visited:
            continue
        if u == dest:
            return dist
        visited.add(u)
        for v in sorted(graph[u]):
            if v not in visited:
                queue.append((v,dist+1))
    return dist

bacons = [0 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            bacons[i] += bfs(i,j)
# print(bacons)
print(bacons[1:].index(min(bacons[1:]))+1)
