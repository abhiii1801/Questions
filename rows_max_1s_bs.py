#https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m = len(arr)
        n = len(arr[0])
        
        max_row = -1
        
        row = 0
        col = n - 1
        while row < m and col>=0:
            if arr[row][col] == 1:
                max_row = row
                col-=1
            else:
                row+=1
            
        
        return max_row
        