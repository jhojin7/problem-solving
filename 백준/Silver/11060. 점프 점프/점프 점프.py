import collections
N=int(input())
A=list(map(int,input().split()))
# dp=[0 for _ in range(N+2)]
# print(dp)

queue = collections.deque([(0,0)]) # i, moves
visited=set()
ok=False
while queue:
    i,moves = queue.popleft()
    if i==N-1:
        ok=True
        break
    if i in visited: continue
    visited.add(i)
    for j in range(A[i]+1):
        if i+j not in visited:
            queue.append((i+j,moves+1))

if not ok: print(-1)
else: print(moves)