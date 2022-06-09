"""
wrong: https://www.acmicpc.net/source/44338142
https://www.acmicpc.net/problem/12865
https://cocoon1787.tistory.com/206
"""
import sys
from io import StringIO
testcases = """
4 7
6 13
4 8
3 6
5 12
""".strip()
# https://stackoverflow.com/a/5062926/3413574
# https://stackoverflow.com/a/34168892/3413574
sys.stdin = StringIO(testcases)
############################################################
# 0-1 knapsack
things = []
N, K = map(int,input().split())
for _ in range(N):
    weight,value = map(int,input().split())
    things.append((weight,value))
# print(N,K,things)

# dp
dp = []
# first row
dp.append([0 for _ in range(K+1)])
for i in range(1,N+1):
    # init row
    dp.append([0 for _ in range(K+1)])
    for j in range(1,K+1):
        if i == 0 or j == 0:
            continue # dp[i][j] = 0
        else:
            # find max from possible values:
            # all combos of things under max weight K
            prev_max = dp[i-1][j]
            if j-things[i-1][0] >= 0: # things[] is 0-indexed
                # if dp[3][7], then cur = 
                #   dp[3][7-(weight of things3)]+(value of thing3)
                cur_bag_weight = j-things[i-1][0]
                cur = dp[i][cur_bag_weight]+things[i-1][1]
                dp[i][j] = max(prev_max, cur)
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp[i])
print(dp[-1][-1])