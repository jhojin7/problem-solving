import collections
visited = [False for _ in range(100001)]
prev = [0 for _ in range(100001)]
def bfs(src,dest):
    queue = collections.deque([(src,0)]) #x,t
    while queue:
        x,t = queue.popleft()
        if not 0<=x<=100000: continue
        if x==dest: return

        if 0<= x*2 <= 100000 and not visited[x*2]:
            visited[x*2] = True
            prev[x*2] = x
            queue.append((x*2,t+1))
        if 0<= x-1 <= 100000 and not visited[x-1]:
            visited[x-1] = True
            prev[x-1] = x
            queue.append((x-1,t+1))
        if 0<= x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = True
            prev[x+1] = x
            queue.append((x+1,t+1))

N,K = map(int,input().split())
bfs(N,K)

ans = []
xx = K
while xx!=N:
    ans.append(xx)
    xx = prev[xx]
ans.append(xx)
ans.reverse()
print(len(ans)-1)
print(*ans)