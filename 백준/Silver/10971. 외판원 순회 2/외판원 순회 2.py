import itertools
import math
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
# print(W)

ans = math.inf
combs = itertools.permutations(range(1, N))
for comb in combs:
    comb = list(comb)+[0]
    dist = 0
    nxt = 0
    for i in comb:
        d = W[nxt][i]
        if d == 0:
            dist = math.inf
            break
        dist += d
        nxt = i
    ans = min(ans, dist)
print(ans)
