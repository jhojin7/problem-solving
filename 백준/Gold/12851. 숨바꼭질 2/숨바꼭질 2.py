import collections,math
def bfs(src,dest):
    # ans = collections.defaultdict(int)
    ans = []
    min_t = math.inf
    cnt = 0
    queue = collections.deque([(src,0)]) #x,t
    visited = set()
    while queue:
        x,t = queue.popleft()
        # if x==2:
        #     print(visited)
        #     print(queue)
        if not 0<=x<=100000: continue
        # if x in visited: continue

        if x == dest:
            # print(t)
            if min_t == math.inf:
                min_t = t
                cnt+=1
            elif min_t == t:
                cnt+=1
            continue
        visited.add(x)

        if 0<=x+1<=100000 and x+1 not in visited:
            queue.append((x+1,t+1))
        if 0<=x-1<=100000 and x-1 not in visited:
            queue.append((x-1,t+1))
        if 0<=x*2<=100000 and x*2 not in visited:
            queue.append((x*2,t+1))
    return min_t,cnt

N,K = map(int,input().split())
ans = bfs(N,K)
print(*ans,sep='\n')