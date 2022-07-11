import sys, collections
input = sys.stdin.readline
N = int(input())
graph = collections.defaultdict(list)
for i in range(N-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
# print(graph)

def bfs(src):
    queue = collections.deque([(src,0)])
    visited = set()
    dest,maxdist = -1,-1
    while queue:
        u,dist = queue.pop()
        # print(u,dist)
        if dist > maxdist:
            dest,maxdist = u,dist
        visited.add(u)
        for v,w in graph[u]:
            if v not in visited:
                queue.append((v,dist+w))
    return (dest, maxdist)

# distance d1 from any node to furthest x
x,d1 = bfs(1) # any src is ok
# distance d2 from x to furthest y
y,d2 = bfs(x) 
print(d2)