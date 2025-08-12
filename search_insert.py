# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pos = 0

        while start<=end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                pos = mid + 1
                start = mid + 1
            else:
                pos = mid
                end = mid -1
        
        return pos


        