"""
id: 1463
ac:https://www.acmicpc.net/source/45596118
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
""".strip())

n = int(input())
dp = [9999999 for _ in range(n+1)]
dp[n] = 0
for x in range(n,0,-1):
    if x%3 == 0:
        dp[x//3] = min(dp[x//3],dp[x]+1)
    if x%2 == 0:
        dp[x//2] = min(dp[x//2],dp[x]+1)
    dp[x-1] = min(dp[x-1],dp[x]+1)
print(dp[1])