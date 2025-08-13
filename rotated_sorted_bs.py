#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start = 0
        end = len(arr) - 1
        while start<=end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[start] <= arr[mid]: #sorted left
                if (arr[start]<=target<=arr[mid]):
                    end = mid-1
                else:
                    start = mid+1
            else: #sorted right
                if (arr[mid]<=target<=arr[end]):
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1


