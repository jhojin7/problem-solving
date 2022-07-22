import sys,collections
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = collections.defaultdict(list)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
# bfs
visited = set()
queue = collections.deque([(1,0)])
while queue:
    u,dist = queue.popleft()
    if dist==3: break
    visited.add(u)
    for v in graph[u]:
        queue.append((v,dist+1))
visited.discard(1)
print(len(visited))