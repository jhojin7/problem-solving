"""
id: 9251
title:LCS
ac:https://www.acmicpc.net/source/44989565
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
acaykp
capcak
""".strip())

import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
# print(s1, s2)

# dp = [[0]*(len(s2)+1)]*(len(s1)+1)
#??????
dp = [[0 for _ in range(len(s2)+1)] 
        for _ in range(len(s1)+1)]
for i in range(len(s1)+1):
    for j in range(len(s2)+1):
        if i==0 or j==0:
            dp[i][j] = 0
        elif s1[i-1] == s2[j-1]:
            # if same, add 1 to diagonal value
            dp[i][j] = dp[i-1][j-1]+1
        else:
            # set dp as max between [i][j-1],[i-1][j],
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(i,">",dp[i])
print(dp[-1][-1])