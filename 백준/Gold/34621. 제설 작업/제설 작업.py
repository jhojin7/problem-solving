N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


def check(arr, p):
    rowsum = [sum(arr[i]) for i in range(N)]
    colsum = [sum(arr[i][j] for i in range(N)) for j in range(M)]
    row_clear = [False for _ in range(N)]
    col_clear = [False for _ in range(M)]
    q = []

    for i in range(N):
        if rowsum[i] <= p:
            q.append(("r", i))
            row_clear[i] = True
    for j in range(M):
        if colsum[j] <= p:
            q.append(("c", j))
            col_clear[j] = True

    while q:
        t, idx = q.pop(0)
        if t == "r":
            for j in range(M):
                if not col_clear[j]:
                    colsum[j] -= arr[idx][j]
                    if colsum[j] <= p:
                        q.append(("c", j))
                        col_clear[j] = True
        else:
            for i in range(N):
                if not row_clear[i]:
                    rowsum[i] -= arr[i][idx]
                    if rowsum[i] <= p:
                        q.append(("r", i))
                        row_clear[i] = True

    if all(row_clear) and all(col_clear):
        return True
    else:
        return False


rowsum = [sum(arr[i]) for i in range(N)]
colsum = [sum(arr[i][j] for i in range(N)) for j in range(M)]

start, end = 1, max(max(rowsum), max(colsum)) + 1
while start < end:
    mid = (start + end) // 2
    if check(arr, mid):
        end = mid
    else:
        start = mid + 1
print(start)
