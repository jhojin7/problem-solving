import sys; input = sys.stdin.readline
import heapq, collections, itertools, math

N,M,K = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]

color = collections.defaultdict(list)
for i in range(N):
    for j in range(M):
        color[(i%K,j%K)].append(grid[i][j])

ans=0
for i in range(K):
    for j in range(K):
        cnter = collections.Counter(color[(i,j)])
        x = (cnter.most_common(1)[0][0])
        y = (cnter.most_common(1)[0][1])
        ans+=len(color[(i,j)])-y
        color[(i,j)] = x

for i in range(N):
    for j in range(M):
        grid[i][j] = color[(i%K,j%K)]

print(ans)
for row in grid:
    print(*row,sep='')
