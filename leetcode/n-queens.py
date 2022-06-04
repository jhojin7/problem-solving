"""
"""
from __solver import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens,i,j):
            # not in board
            if not (0<=i<=n-1 and 0<=j<=n-1):
                return False
            # check horizontal, vertical
            if (i in queens.keys()
                or j in queens.values()):
                return False
            # check diagonals
            for x in queens:
                y = queens[x]
                slope = (y-j)/(x-i)
                print((x,y),(i,j),abs(slope))
                if abs(slope) == 1:
                    return False

            # visit
            print("dfs",i,j,queens.values())
            queens[i] = j
            # if n queens successfully found
            if len(queens) == n:
                ans_queens.append(queens)
            # dfs into cols in next row
            for col in range(n):
                print("dfs into ",queens, (i+1,col))
                dfs(queens,i+1,col)

        def make_board(queens:dict)->List[str]:
            board = []
            for i in range(n):
                tmp = []
                for j in range(n):
                    if queens[i]==j: 
                        tmp.append('Q') 
                    else: 
                        tmp.append('.')
                board.append("".join(tmp))
            return board

        #####################
        # try dfs from all cols in first row
        ans_queens = []
        for a in range(n):
            # dfs({},0,a)
            dfs({0:0},1,a)
            # # if n queens successfully found
            # if len(queens) == n:
            #     ans_queens.append(queens)
        print(ans_queens)
        # make board
        ret = []
        for queens in ans_queens:
            ret.append(make_board(queens))
        return ret
print(Solution().solveNQueens(5))


output = [
    ["Q....","..Q..","....Q",".Q...","...Q."],
    [".Q...","...Q.","Q....","..Q..","....Q"],
    ["..Q..","Q....","...Q.",".Q...","....Q"],
    ["...Q.","Q....","..Q..","....Q",".Q..."]]
expected = [
    ["Q....","..Q..","....Q",".Q...","...Q."],
    [
    "Q....",
    "...Q.",
    ".Q...",
    "....Q",
    "..Q.."],
    [".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]