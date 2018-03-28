class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0]);
 
        start = 0;
        end = m*n-1;
 
        while start<=end:
            mid = int(start + (end - start)/2)
            midX = int(mid/n)
            midY = int(mid%n)
 
            if matrix[midX][midY]==target:
                return True
 
            if matrix[midX][midY]<target:
                start=mid+1
            else: 
                end=mid-1
 
        return False


class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0 :
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False