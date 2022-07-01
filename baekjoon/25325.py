"""
id: 25325
ac:https://www.acmicpc.net/source/45346929
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
4
aaa bbb ccc ddd
bbb ddd
aaa ddd
aaa
aaa bbb
""".strip())

import sys, collections
input = sys.stdin.readline

n = int(input())
names = input().split()
cnt = collections.defaultdict(int)
likes = []
for _ in range(n):
    likes.extend(input().rsplit())
for name in names:
    cnt[name] = 0
for name in likes:
    cnt[name] += 1

for k,v in sorted(cnt.items(),key=lambda x: (-x[1],x[0])):
    print(k,v)