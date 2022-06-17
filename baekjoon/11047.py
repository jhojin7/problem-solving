"""
title:11047 동전0
ac: https://www.acmicpc.net/source/44659993
"""

tc = """
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""
from io import StringIO
import sys
sys.stdin = StringIO(tc.strip())

N, K = map(int,input().split())
coins = []
for _ in range(N):
    c = int(input())
    # if coin > K, no need
    if c > K: continue
    else: coins.append(c)
# reverse coins
coins.sort(reverse=True)
# print(N, K, coins)

cnt, i = 0, 0
while K > 0:
    # move i until coins[i] is smaller than K
    while K < coins[i]:
        i += 1
    # print(cnt,K,'-',coins[i])
    K -= coins[i]
    cnt += 1
    # if coins[i] is smaller than K,
    # move to smaller coin
    if K < coins[i]:
        i += 1
print(cnt)
