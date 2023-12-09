N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
ans = ""
acgts = []
for j in range(M):
    d = 0
    acgt = [0, 0, 0, 0]
    for i in range(N):
        acgt["ACGT".index(arr[i][j])] += 1
    ans += "ACGT"[acgt.index(max(acgt))]

ham = 0
for x in arr:
    for i in range(M):
        if x[i] != ans[i]:
            ham += 1
print(ans)
print(ham)
