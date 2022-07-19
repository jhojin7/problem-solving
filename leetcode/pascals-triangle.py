from __solver import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        pascal = [[1],[1,1]]
        for r in range(2,numRows):
            row = [1]
            for i in range(len(pascal[r-1])-1):
                x = pascal[r-1][i]+pascal[r-1][i+1]
                row.append(x)
            row.append(1)
            pascal.append(row)
        print(pascal)
        return pascal
Solution().generate(2)