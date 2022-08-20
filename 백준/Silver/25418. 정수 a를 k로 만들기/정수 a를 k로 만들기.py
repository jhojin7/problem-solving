import collections
a,k = map(int,input().split())
queue = collections.deque([(a,0)])
visited = set()
while queue:
    x,cnt = queue.popleft()
    if x==k: 
        # print(x,cnt)
        print(cnt)
        break
    visited.add(x)
    if a<=x*2<=2000000 and x*2 not in visited:
        queue.append((x*2,cnt+1))
    if a<=x+1<=2000000 and x+1 not in visited:
        queue.append((x+1,cnt+1))