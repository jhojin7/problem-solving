N=int(input())
import collections
q=collections.deque(range(1,N+1))
while q:
    x=q.popleft()
    print(x,end=' ')
    if q: q.append(q.popleft())