"""
id: 25326
ac:https://www.acmicpc.net/source/45351178
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5 4
kor apple red
kor pear blue
eng apple red
eng orange blue
math apple green
kor apple red
kor - blue
eng - -
- - red
""".strip())

import sys
input = sys.stdin.readline
subjects = ['kor', 'eng', 'math']
fruits = ['apple', 'pear', 'orange']
colors = ['red', 'blue', 'green']
data = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0],[0,0,0],[0,0,0]]]

n,m = map(int,input().split())
for _ in range(n):
    subj,fruit,color = input().split()
    i = subjects.index(subj)
    j = fruits.index(fruit)
    k = colors.index(color)
    data[i][j][k] += 1

for _ in range(m):
    subj,fruit,color = input().split()
    if subj != '-':
        i = subjects.index(subj)
        i = range(i,i+1)
    else:
        i = range(3)
    if fruit != '-':
        j = fruits.index(fruit)
        j = range(j,j+1)
    else:
        j = range(3)
    if color != '-':
        k = colors.index(color)
        k = range(k,k+1)
    else:
        k = range(3)
    # print(i,j,k)

    sum = 0
    for a in i:
        for b in j:
            for c in k:
                # print((a,b,c),data[a][b][c])
                sum += data[a][b][c]
    print(sum)
    