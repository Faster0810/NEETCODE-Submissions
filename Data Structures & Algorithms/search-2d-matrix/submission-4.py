class Solution:
    def searchMatrix(self, matrix, target):

        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        # find correct row
        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2

        # binary search in row
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False