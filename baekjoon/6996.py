"""
id: 6996
title:애너그램
ac:https://www.acmicpc.net/source/45307802
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    str1,str2 = map(str,input().split())
    if sorted(str1) == sorted(str2):
        print("{} & {} are anagrams.".format(str1,str2))
    else:
        print("{} & {} are NOT anagrams.".format(str1,str2))