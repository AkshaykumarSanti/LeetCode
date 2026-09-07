class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for k in range(len(matrix)):
            i = 0
            j = len(matrix[k]) - 1
            while i <= j:
                mid = (i+j) // 2
                if matrix[k][mid] == target:
                    return True
                elif matrix[k][mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
        
        return False