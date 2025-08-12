# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        
        start, end = 0, len(arr) - 1
        first_occur = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                first_occur = mid
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        start, end = 0, len(arr) - 1
        last_occur = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                last_occur = mid
                start = mid + 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        if first_occur == -1:
            return 0
        
        return last_occur - first_occur + 1

