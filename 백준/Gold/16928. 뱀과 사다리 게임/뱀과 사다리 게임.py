import collections
N,M = map(int,input().split())
snake = {}
for _ in range(N+M):
    v,w = map(int,input().split()) 
    snake[v] = w
if len(snake)==0:
    print(100//6)
    exit()

vis = set()
q = collections.deque([(1,0)])
while q:
    cur,cnt = q.popleft()
    if cur==100:
        print(cnt)
        exit()
    for i in range(1,7):
        if cur+i > 100: continue
        elif cur+i in snake.keys():
            next=cur+i
            while next in snake.keys():
                next = snake[next]
            q.append((next,cnt+1))
        else:
            if cur+i in vis: continue
            vis.add(cur+i)
            q.append((cur+i,cnt+1))