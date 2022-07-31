import collections
N = int(input())
prev = collections.defaultdict()

q = collections.deque([(N,0)])
visited = set()
while q:
    x,cnt = q.popleft()
    # print(x,prev)
    if x in visited: continue 
    visited.add(x)
    if x==1:
        print(cnt)
        break

    if x%3==0 and x//3 not in visited:
        if x//3 not in prev.keys():
            prev[x//3] = x
        q.append((x//3,cnt+1))
    if x%2==0 and x//2 not in visited:
        # if x//2 in visited: continue
        if x//2 not in prev.keys():
            prev[x//2] = x
        q.append((x//2,cnt+1))
    if 0<x-1 and x-1 not in visited:
        # if x-1 in visited: continue
        if x-1 not in prev.keys():
            prev[x-1] = x
        q.append((x-1,cnt+1))

ans = []
cur = 1
while cur!=N:
    ans.append(cur)
    cur = prev[cur]
ans.append(cur)
ans.reverse()
print(*ans)