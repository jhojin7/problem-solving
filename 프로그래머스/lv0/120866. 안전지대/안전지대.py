dxy = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
def solution(board):
    n,m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j]!=1: continue
            for dx,dy in dxy:
                nx,ny = i+dx,j+dy
                if not (0<=nx<n and 0<=ny<m):
                    continue
                if board[nx][ny]==1:
                    continue
                board[nx][ny] = 2
    ans = 0
    for b in board:
        ans+=b.count(0)
            
    return ans
