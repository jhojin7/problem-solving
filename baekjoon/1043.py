"""
id: 1043
title:거짓말
ac:https://www.acmicpc.net/source/45242278
"""
import sys
from io import StringIO
# 4 2
# 1 4
# 3 1 3
# 2 1 4
sys.stdin = StringIO("""
5 5
1 1
0 4 5
0 3 4
0 2 3
0 1 2
0 1 
""".strip())

import sys
N,M = map(int,input().split())
avoid = list(map(int,input().split()))[1:]
avoid = set(avoid)
print(avoid)
parties = []
for _ in range(M):
    party = list(map(int,input().split()))[1:]
    party = set(party)
    parties.append(party)
for _ in range(M):
    for party in parties:
        for x in party:
            if x in avoid:
                avoid.update(party)
                break
# print(avoid)
print(parties)
assert len(parties) == M
ans = M
for party in parties:
    print(party,avoid)
    print("isdisjoint",party.isdisjoint(avoid))
    for x in party:
        if x in avoid:
            print(x,avoid)
            ans -= 1
            break
print()
print(ans,avoid)


# print(*range(1,51),sep=' ')