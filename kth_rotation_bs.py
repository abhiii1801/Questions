#https://www.geeksforgeeks.org/problems/rotation4723/1

class Solution:
    def findKRotation(self, nums):
        # code here
        
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:  
                start = mid + 1
            else:
                end = mid
        
        return start
            
            
            
        
