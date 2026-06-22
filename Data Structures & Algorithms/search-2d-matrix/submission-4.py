class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowL, rowR = 0, ROWS - 1
        colL, colR = 0, COLS - 1

        while rowL <= rowR:
            midRow = (rowL+rowR) // 2

            if target >= matrix[midRow][0] and target <= matrix[midRow][COLS-1]:
                while colL <= colR:
                    midCol = (colL+colR) // 2
                    
                    if target > matrix[midRow][midCol]:
                        colL = midCol+1
                    elif target < matrix[midRow][midCol]:
                        colR = midCol-1
                    else:
                        return True
                return False
            elif target > matrix[midRow][COLS-1]:
                rowL = midRow+1
            elif target < matrix[midRow][0]:
                rowR = midRow-1
        
        return False