"""
https://leetcode.com/submissions/detail/712619064/
"""
from __solver import *
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transposed = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed
# matrix = [[1,2,3],[4,5,6]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(matrix))