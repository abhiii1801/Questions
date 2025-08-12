#https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        row = 0
        col = n - 1

        while(row < m and col >= 0):
            if target == mat[row][col]:
                return True
            elif target < mat[row][col]:
                col-=1
            elif target > mat[row][col]:
                row+=1
        
        return False

