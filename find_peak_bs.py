#https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binary_search(arr, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            left = False
            if mid == 0:
                left = True
            elif arr[mid] > arr[mid - 1]:
                left = True

            right = False
            if mid == end:
                right = True
            elif arr[mid] > arr[mid + 1]:
                right = True
            
            if left and right:
                return mid
            
            if arr[mid] < arr[mid + 1]:
                return binary_search(arr, mid + 1, end)
            else:
                return binary_search(arr, start, mid - 1)

        return binary_search(nums, 0, len(nums) - 1)
