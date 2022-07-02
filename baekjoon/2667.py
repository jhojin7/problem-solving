"""
id: 2667
title:단지번호붙이기
ac: https://www.acmicpc.net/source/45408383
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys, collections
def bfs(_apt,_i,_j):
    apt_cnt = 0
    queue = collections.deque([(_i,_j)])
    diff = [(-1,0),(1,0),(0,-1),(0,1)]
    # print("_apt",_apt,_i,_j)
    while queue:
        # visit
        (visit_i, visit_j) = queue.popleft()
        # if cell was visited, don't visit
        if int(mat[visit_i][visit_j]) < 1: continue
        apt_cnt += 1#;print("aptcnt",apt_cnt,visit_i,visit_j,mat[visit_i][visit_j])
        mat[visit_i][visit_j] = _apt
        # append
        for di, dj in diff:
            new_i, new_j = visit_i+di, visit_j+dj
            if ((0<=new_i<N and 0<=new_j<N)
                and mat[new_i][new_j] == '1'):
                queue.append((new_i, new_j))
    return apt_cnt

N = int(input())
global mat
mat = []
for _ in range(N):
    row = map(str,sys.stdin.readline().strip())
    mat.append([*row])

# start bfs on all '1' cells
# visited cells = -1,-2,...
apt = 0 # return abs(apt) when finished
apt_result = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == '1':
            apt -= 1 # change apt number -(1,2,3,...)
            apt_result.append(bfs(str(apt),i,j))

apt_result.sort()
print(len(apt_result))
# for i in range(len(apt_result)):
#     print(apt_result[i][1])
for n in apt_result: print(n)