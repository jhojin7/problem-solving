import itertools, collections, copy

N, M = map(int, input().split())
_arr = [list(map(int, input().split())) for _ in range(N)]
zeros = [(i, j) for i in range(N) for j in range(M) if _arr[i][j] == 0]
perms = itertools.combinations(zeros, 3)


def bfs(xx, yy):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = collections.deque()
    vis = set()
    q.append((xx, yy))
    while q:
        x, y = q.popleft()
        if (x, y) in vis:
            continue
        vis.add((x, y))
        arr[x][y] = 2
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < N:
                continue
            if not 0 <= ny < M:
                continue
            if arr[nx][ny] == 0:
                q.append((nx, ny))


def run():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                bfs(i, j)
    tmpcnt = 0
    for row in arr:
        tmpcnt += row.count(0)
    return tmpcnt


ans = -(9**999)
for perm in perms:
    arr = copy.deepcopy(_arr)
    for x, y in perm:
        arr[x][y] = 1
    cnt = run()
    ans = max(ans, cnt)
    for x, y in perm:
        arr[x][y] = 0
print(ans)
