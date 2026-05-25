class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        row = -1

        # identify the row where our target is
        for i in range(ROWS):
            if target >= matrix[i][0] and target <= matrix[i][COLS-1]:
                row = i
        if row == -1:
            return False
        l, r = 0, COLS-1
        while l <= r:
            mid = (l+r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid-1
        return False

        
