#https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return nums[-1]
        while start<=end:
            mid = (start + end) // 2
            first_occur = None
            if mid!=end:
                if nums[mid] == nums[mid+1]:
                    first_occur = mid
            if mid!=start:
                if nums[mid] == nums[mid-1]:
                    first_occur = mid-1
            if first_occur == None:
                return nums[mid]
            if first_occur % 2 == 0:
                start = first_occur + 2
            else:
                end = first_occur - 1
            
            
