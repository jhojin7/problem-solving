"""
id: 2577
title:숫자의개수
ac:https://www.acmicpc.net/source/44703708 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys, collections
A = int(input())
B = int(input())
C = int(input())
D = A*B*C
cnt = collections.Counter(str(D))
# print(cnt,str(D))
for i in range(10):
    if str(i) not in cnt:
        print(0)
    else:
        print(cnt[str(i)])