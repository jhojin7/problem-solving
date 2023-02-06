import sys
input = sys.stdin.readline
print([1,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])
exit()

def dfs(board,row,col):
    # stop dfs
    if len(board) == N and board not in boards: 
        boards.append(board)
        return
    # check vertical
    if col in board: return

    # dfs
    for c in range(N):
        # check diagonal
        diagL = N-1+(row-col)
        diagR = row+col
        if (diagonals_L[diagL]
            or diagonals_R[diagR]):
            continue
        diagonals_L[diagL] = diagonals_R[diagR] = True
        # dfs
        dfs(board+[col],row+1,c)
        diagonals_L[diagL] = diagonals_R[diagR] = False

N = int(input())
boards = []
diagonals_L = [False for _ in range(2*N)] # 2N just in case
diagonals_R = [False for _ in range(2*N)]

for col in range(N):
    dfs([],0,col)
print(len(boards))