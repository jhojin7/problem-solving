"""
id: 1149
ac:https://www.acmicpc.net/source/45347794
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3
1 2 3
1 2 3
1 2 3
""".strip())

import sys
input = sys.stdin.readline
N = int(input())
dp = []
dp.append([0,0,0])
for _ in range(N):
    house = map(int,input().split())
    dp.append(list(house))

for i in range(1,N+1):
    dp[i][0] += min(dp[i-1][1],dp[i-1][2])
    dp[i][1] += min(dp[i-1][0],dp[i-1][2])
    dp[i][2] += min(dp[i-1][0],dp[i-1][1])

# print(dp)
print(min(dp[-1]))