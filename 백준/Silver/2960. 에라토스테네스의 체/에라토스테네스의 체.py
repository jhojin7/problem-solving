N, K = map(int, input().split())

arr = [True for i in range(N+1)]
arr[0] = False
cnt = 0

for i in range(2, N+1):
    if not arr[i]:
        continue
    for j in range(i, N+1, i):
        if not arr[j]:
            continue
        arr[j] = False
        cnt += 1
        if cnt == K:
            print(j)
            exit()
