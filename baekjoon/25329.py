"""
id: 25329
ac:https://www.acmicpc.net/source/45342514
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys, collections, math
input = sys.stdin.readline

n = int(input())
students = collections.defaultdict(int)
for _ in range(n):
    timestamp, name = input().split()
    hh,mm = map(int,timestamp.split(":"))
    if hh>0: mm += 60*hh
    # print(mm,name)

    if not students[name]:
        students[name] = mm
    else:
        students[name] += mm
# print(students)

ans = []
for name in students.keys():
    cost = 10
    mins = students[name]-100
    # print(name,mins,mins/50)
    if mins >= 50:
        cost += 3*(mins//50)
    elif mins < 0:
        ans.append((name,cost))
        continue
    if mins%50 > 0:
        cost += 3
    ans.append((name,cost))

for stu in sorted(ans,key=lambda x:(-x[1],x[0])):
    print(*stu)
        

