class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False
