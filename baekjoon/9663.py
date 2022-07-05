"""
id: 9663
ac:https://www.acmicpc.net/source/45530960
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
14
""".strip())

import sys
input = sys.stdin.readline
# print([1,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])
# exit()

# def dfs(board,row,col):
#     global cnt
#     # stop dfs
#     if len(board) == N and tuple(board) not in boards: 
#         boards.add(tuple(board))
#         cnt += 1
#         return
#     # check vertical
#     if col in board: return

#     # dfs
#     for c in range(N):
#         # check diagonal
#         diagL = N-1+(row-col)
#         diagR = row+col
#         if (diagonals_L[diagL]
#             or diagonals_R[diagR]):
#             continue
#         diagonals_L[diagL] = diagonals_R[diagR] = True
#         # dfs
#         dfs(board+[col],row+1,c)
#         diagonals_L[diagL] = diagonals_R[diagR] = False

# N = int(input())
# boards = set()
# diagonals_L = [False for _ in range(2*N)] # 2N just in case
# diagonals_R = [False for _ in range(2*N)]
# cnt = 0

# for col in range(N):
#     dfs([],0,col)
# print(len(boards),cnt)


def promising(row)->bool:
    for i in range(row):
        if (board[row] == board[i]
            or abs(board[row]-board[i]) == row-i):
            return False
    return True

def queens(row):
    global cnt
    if row==N:
        cnt +=1
        return
    else:
        for i in range(N):
            board[row] = i
            if promising(row):
                queens(row+1)

board = [0 for _ in range(14)]
cnt = 0
N = int(input())
queens(0)
print(N,cnt)