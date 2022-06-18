"""
id: 1992
title:쿼드트리
ac:https://www.acmicpc.net/source/44686950
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
""".strip())

def quad(_mat,n):
    # exit recursion
    if n == 1: return _mat[0][0]
    # split into quads 
    # 왼쪽위 오른쪽위 왼쪽아래 오른쪽아래
    half = n//2
    mat1 = [_mat[i][:half] for i in range(half)]
    mat2 = [_mat[i][half:] for i in range(half)]
    mat3 = [_mat[i][:half] for i in range(half,n)]
    mat4 = [_mat[i][half:] for i in range(half,n)]
    # print(half,mat1,mat2,mat3,mat4,sep='\n')
    # quad recurse down
    quad1 = quad(mat1,half)
    quad2 = quad(mat2,half)
    quad3 = quad(mat3,half)
    quad4 = quad(mat4,half)
    # print(quad1,quad2,quad3,quad4,sep='\t')
    # gather return values
    if ''.join([quad1,quad2,quad3,quad4]) == "1111":
        return "1"
    elif ''.join([quad1,quad2,quad3,quad4]) == "0000":
        return "0"
    # if not "1111" or "0000", return with ()
    return "({}{}{}{})".format(
            quad1,quad2,quad3,quad4)

import sys
N = int(input())
mat = []
for _ in range(N):
    row = sys.stdin.readline().rstrip()
    # print(row.rstrip())
    mat.append(row)
print(quad(mat,N))