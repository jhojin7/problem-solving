"""
https://leetcode.com/submissions/detail/711776723/
"""
from __solver import *
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start from matrix[0][-1]
        row, col = 0, len(matrix[0])-1
        # find target
        while row < len(matrix) and col >= 0:
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return False

    def bruteforce(self, matrix: List[List[int]], target: int) -> bool:
        # print(any(x for row in matrix for x in row))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[17,30,34,60]]
target = 34
print(Solution().searchMatrix(matrix,target))
