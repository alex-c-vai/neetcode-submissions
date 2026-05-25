class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        bot, top = 0, ROWS-1
        row = -1

        # identify the row where our target is
        while bot <= top:
            mid = (top + bot) // 2
            if target <= matrix[mid][COLS-1] and target >= matrix[mid][0]:
                row = mid
                break
            elif target <= matrix[mid][0]:
                top = mid - 1
            else:
                bot = mid + 1
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

        
