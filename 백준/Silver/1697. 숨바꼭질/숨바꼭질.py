import collections

def bfs(src,dest):
    queue = collections.deque([(0,src)])
    visited = set()
    cnt = 0
    while queue:
        cnt,cur = queue.popleft()
        if not 0<= cur <= 100000: continue
        if cur in visited: continue

        visited.add(cur)
        if cur==dest: 
            return cnt
        
        to_add = []
        if 0<= cur*2 <= 100000:
            to_add.append((cnt+1,cur*2))
        if 0<= cur-1 <= 100000:
            to_add.append((cnt+1,cur-1))
        if 0<= cur+1 <= 100000:
            to_add.append((cnt+1,cur+1))
        queue.extend(to_add)

src,dest = map(int,input().split())
print(bfs(src,dest))