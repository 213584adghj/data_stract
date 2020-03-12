class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:  
            return False
        m=len(matrix)
        n=len(matrix[0])
        i=m-1
        j=0
        while(i>=0 and j<n):
            if(matrix[i][j]==target):
                return True
            if(matrix[i][j]>target):
                i=i-1
            if(matrix[i][j]<target):
                j=j+1
        return False