#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    first = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return first

        def find_last(nums, target):
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    last = mid
                    start = mid + 1  # go right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last

        return [find_first(nums, target), find_last(nums, target)]
