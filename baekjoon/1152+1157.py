"""
id: 1152+1157
title:단어의개수
ac: https://www.acmicpc.net/source/44701744
https://www.acmicpc.net/source/44702242
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
zZajjjjj
""".strip())


# import sys;print(len(sys.stdin.read().split()))

from collections import Counter
word = input().upper()
if len(word) == 1: 
    print(word)
    exit()
cnt = Counter(word).most_common(2)
# print(cnt)
if (cnt[0][0] != cnt[1][0]
    and cnt[0][1] == cnt[1][1]):
    print("?")
else: print(cnt[0][0])
