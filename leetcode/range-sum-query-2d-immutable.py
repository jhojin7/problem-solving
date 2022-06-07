"""
accepted:https://leetcode.com/submissions/detail/716673231/
tle:https://leetcode.com/submissions/detail/713373913/
IndexError:https://leetcode.com/submissions/detail/713395396/
https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/2104545/O(m*n)-to-O(n)-to-O(1)-Search-Time-oror-C++
"""
from __solver import *
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat1 = matrix
        self.mat2 = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.mat2[i][j] = \
                self.mat1[i-1][j-1]\
                + self.mat2[i-1][j]\
                + self.mat2[i][j-1]\
                - self.mat2[i-1][j-1]
        print(self.mat2)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(row1,col1,row2,col2)
        return self.mat2[row2+1][col2+1]\
            - self.mat2[row1][col2+1]\
            - self.mat2[row2+1][col1]\
            + self.mat2[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]

obj = NumMatrix(matrix)
row1,col1,row2,col2 = [2,1,4,3]
tc = testcases("""
[2,1,4,3]
[1,1,2,2]
[1,2,2,4]
""")
while tc:
    param_1 = obj.sumRegion(*tuple(*tc.popleft()))
    print(param_1)