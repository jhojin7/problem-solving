"""
id: 18870
title:좌표압축
ac:https://www.acmicpc.net/source/45282317
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5
1 1 2 1 0
""".strip())

import sys,collections
input = sys.stdin.readline
N = int(input())
X = list(map(int,input().split()))

counted = collections.Counter(X)
counted_keys = collections.Counter(counted.keys())
print(counted_keys)
s = 0
for x,cnt in sorted(counted_keys.items()):
    counted[x] = s
    s += cnt
print(counted)

for x in X:
    sys.stdout.write(str(counted[x])+' ')