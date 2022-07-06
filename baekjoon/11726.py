"""
id: 11726
ac:https://www.acmicpc.net/source/45599326
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
6
""".strip())

n=int(input())
dp = [0 for _ in range(n+3)]
dp[1],dp[2] = 1,2
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%10007
print(dp[n])