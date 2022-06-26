"""
id: 15650
title:N과M(2)
ac:https://www.acmicpc.net/source/45045765
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
4 4
1 1 2 2
""".strip())

import itertools
N,M = map(int,input().split())
lists = itertools.combinations(range(1,N+1),M)
for l in lists: print(*l,sep=' ')