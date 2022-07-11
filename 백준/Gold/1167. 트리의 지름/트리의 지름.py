import sys, collections
input = sys.stdin.readline
N = int(input())
graph = collections.defaultdict(list)
for _ in range(1,N+1):
    a,*line,_ = map(int,input().split())
    for i in range(0,len(line)-1,2):
        graph[a].append((line[i],line[i+1]))
    graph[a].sort(key=lambda x:-x[1])

def bfs(src):
    queue = collections.deque([(src,0)])
    visited = set()
    dest,maxdist = -1,-1
    while queue:
        u,dist = queue.pop()
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