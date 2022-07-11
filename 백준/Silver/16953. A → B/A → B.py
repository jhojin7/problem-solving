import sys, collections
input = sys.stdin.readline

A,B = map(int,input().split())
ans = []
queue = collections.deque([(A,1)])
while queue:
    n,cnt = queue.pop()
    if n==B: ans.append((n,cnt))
    # *2
    n1 = n*2
    # *10+1
    n2 = n*10+1
    if 1<=n1<=10**9: queue.append((n1,cnt+1))
    if 1<=n2<=10**9: queue.append((n2,cnt+1))
# print(ans)
if len(ans) == 0: print(-1)
else: print(ans[0][1])