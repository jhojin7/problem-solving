N, S = map(int, input().split())
arr = list(map(int, input().split()))
presum = [0 for _ in range(N + 1)]
# presum[0] = arr[0]
# for i in range(1, N):
#     presum[i] = presum[i - 1] + arr[i]
for i in range(N):
    presum[i + 1] = presum[i] + arr[i]
# presum[N] = presum[N - 1]

l, r = 0, 0
ans = 9**100

flag = False
while l <= r and r < len(arr) + 1:
    ss = presum[r] - presum[l]
    if ss >= S:
        # print(l, r, ss)
        l += 1
        ans = min(ans, r - l + 1)
        flag = True
    else:
        r += 1

if not flag:
    print(0)
else:
    print(ans)
