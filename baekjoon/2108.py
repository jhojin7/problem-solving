"""
id: 2108
ac:https://www.acmicpc.net/source/45581367
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys, collections
mean,median,mode,rangee = 0,0,0,0
n,*arr = map(int,sys.stdin.read().split())
# print(n,arr)

# mode
cnter = collections.Counter(arr).items()
bycount = collections.defaultdict(list)
for item in cnter:
    bycount[item[1]].append(item[0])
# print(bycount.keys(), bycount)
mostfreq = sorted(bycount.keys(),reverse=True)[0]
# print(mostfreq)
if len(bycount[mostfreq]) > 1:
    mode = sorted(bycount[mostfreq])[1]
else:
    mode = bycount[mostfreq][0]

# mean median
mean = round(sum(arr)/n)
median = sorted(arr)[n//2]
# range
rangee = max(arr)-min(arr)

print(mean,median,mode,rangee,sep='\n')