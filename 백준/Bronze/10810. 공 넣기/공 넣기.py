N, M = map(int, input().split())
arr = [0 for _ in range(N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        arr[x] = k
print(*arr[1:], sep=' ')
