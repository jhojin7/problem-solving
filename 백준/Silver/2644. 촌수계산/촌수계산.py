import collections
N=int(input())
src,dest=map(int,input().split())
M=int(input())
tree = collections.defaultdict(list)
for _ in range(M):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = -99
visited = set()
queue = collections.deque([(src,0)])
while queue:
    u,dist = queue.popleft()
    if u==dest:
        ans = dist
        break
    if u in visited:
        continue
    visited.add(u)
    for v in tree[u]:
        if v not in visited:
            queue.append((v,dist+1))

if ans==-99:print(-1)
else:print(ans)