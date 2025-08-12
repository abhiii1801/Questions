#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start_row, end_row = 0, m - 1

        while start_row <= end_row:
            mid_row = start_row + (end_row - start_row) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
                l, r = 0, n - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            elif target < matrix[mid_row][0]:
                end_row = mid_row - 1
            else:
                start_row = mid_row + 1

        return False
