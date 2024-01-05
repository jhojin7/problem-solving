import math
import collections

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
global_vis = [[0 for _ in range(N)] for _ in range(N)]
def is_open(x, y): return True if (L <= abs(x-y) <= R) else False


def bfs(xx, yy):
    q = collections.deque()
    s = 0
    vis = set()
    q.append((xx, yy))
    grp = []
    while q:
        x, y = q.pop()
        if (x, y) in vis:
            continue
        vis.add((x, y))
        grp.append((x, y))
        global_vis[x][y] = 1
        s += arr[x][y]
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if not is_open(arr[x][y], arr[nx][ny]):
                continue
            q.append((nx, ny))
    return grp, s


day = 0
while 1:
    # chk open
    grps = []
    for i in range(N):
        for j in range(N):
            if global_vis[i][j] == 1:
                continue
            grp, s = bfs(i, j)
            grps.append((grp, s))
    # if all closed, return
    if len(grps) == N*N:
        break
    # else, update
    for grp, s in grps:
        for i, j in grp:
            arr[i][j] = s//len(grp)
    for i in range(N):
        for j in range(N):
            global_vis[i][j] = 0
    day += 1

print(day)
