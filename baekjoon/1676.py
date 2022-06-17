"""
id: 1676
title:팩토리얼0의개수
ac: https://www.acmicpc.net/source/44667522
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
19
""".strip())

import math
N = int(input())
fac = list(math.factorial(N).__repr__())

cnt = 0
for i in range(len(fac)-1,-1,-1):
    if fac[i] != '0':
        break
    cnt += 1
print(cnt)