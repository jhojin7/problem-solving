import collections
import heapq
N = int(input())
arr = []
for _ in range(N):
    a, b, c = map(int, input().split())
    arr.append((b, c))
arr.sort()

# print(arr)

ans = 0
pq = []
for i in range(N):
    if len(pq) > 0:
        if pq[0] > arr[i][0]:
            ans += 1
        else:
            heapq.heappop(pq)
    else:
        ans += 1
    heapq.heappush(pq, arr[i][1])
print(ans)
