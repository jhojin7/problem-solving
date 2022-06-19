"""
id: 2178
title:미로탐색
ac:https://www.acmicpc.net/source/44717023
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
4 6
101111
101010
101011
111011
""".strip())

import sys, collections

def not_visited(visited, x,y):
    for (a,b,_) in visited:
        if (a,b) == (x,y):
            return False
    return True

def bfs(_mat):
    # starting point
    start = (0,0,1)
    # diff
    diff = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = collections.deque()
    queue = collections.deque([start])
    while queue:
        # pop
        v = queue.popleft()
        # visit
        visited.append(v)
        _i,_j,_cnt = v
        # append
        for di,dj in diff:
            new_i, new_j = _i+di,_j+dj
            if ((0<=new_i<N and 0<=new_j<M)
                and _mat[new_i][new_j] == '1'):
                # and not_visited(visited, new_i, new_j)):
                queue.append((new_i, new_j ,_cnt+1))
                _mat[new_i][new_j] = 'X'
                if new_i == N-1 and new_j == M-1:
                    return _cnt+1
    # print(queue, visited)

N, M = map(int,sys.stdin.readline().split())
mat = []
for i in range(N):
    row = (sys.stdin.readline().rstrip())
    mat.append([*row])
print(bfs(mat))


"""
def search(_mat,_cnt,i,j):
    # visit
    _mat[i][j] = 'X'
    # print((i,j,_cnt),_mat)

    # if destination
    if i == N-1 and j == M-1:
        return _cnt

    south,east,north,west = 10000,10000,10000,10000
    # deep copy of _mat
    __mat = [row[:] for row in _mat]
    # search east
    if j+1 < M and _mat[i][j+1] == '1':
        east = search(__mat,_cnt+1,i,j+1)
    # search south
    if i+1 < N and _mat[i+1][j] == '1':
        south = search(__mat,_cnt+1,i+1,j)
    # search west
    if j-1 >= 0 and _mat[i][j-1] == '1':
        west = search(__mat,_cnt+1,i,j-1)
    # search north
    if i-1 >= 0 and _mat[i-1][j] == '1':
        north = search(__mat,_cnt+1,i-1,j)

    # return min
    return min([south,east,north,west])

import sys
N, M = map(int,sys.stdin.readline().split())
mat = []
for i in range(N):
    row = (sys.stdin.readline().rstrip())
    mat.append([*row])
# print(mat)
print(search(mat,1,0,0))
"""