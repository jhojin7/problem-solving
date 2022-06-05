"""
https://leetcode.com/submissions/detail/714717461/
https://leetcode.com/submissions/detail/714711918/
"""
from __solver import *
class Solution:
    def totalNQueens(self, n: int) -> int:
        def make_board(queens:list)->List[str]:
            board = []
            for i in range(len(queens)):
                base = ['.']*n
                base[queens[i]] = "Q"
                board.append("".join(base))
            return board

        def dfs(board,i,j):
            # print((i,j),board)
            # board full and new answer
            if (len(board) == n 
            and board not in ans):
                ans.append(board)
                return
            # check horizontal, vertical
            if j in board:
                return
            # check diagonals
            for x in range(i):
                # x,y = all other queens before myself
                x,y = x,board[x] 
                slope = (y-j)/(x-i)
                if abs(slope)==1:
                    return

            for col in range(n):
                # visit and dfs
                dfs(board+[j],i+1,col)
            return
        ######
        ans = []
        for col in range(n):
            dfs([],0,col)
        # return len(ans)
        return [make_board(queens) for queens in ans]

print(Solution().totalNQueens(5))