import collections
M, N, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

ans = []
for i in range(N):
    for j in range(M):
        q = collections.deque([(i, j)])
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cnt = 0
        while q:
            x, y = q.pop()
            if arr[x][y] in [1, -1]:
                continue
            arr[x][y] = -1
            cnt += 1
            if (arr[x][y] == 1):
                continue
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not ((0 <= nx < N) and 0 <= ny < M):
                    continue
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
        if cnt:
            ans.append(cnt)
print(len(ans))
print(*sorted(ans), sep=' ')
