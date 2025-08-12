#https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        n = len(arr)
        floor = -1
        ceil = -1
        start, end = 0, n - 1
        
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == x:
                return [arr[mid], arr[mid]]
            elif arr[mid] < x:
                floor = arr[mid]
                start = mid + 1
            else:
                ceil = arr[mid]
                end = mid - 1
        
        return [floor, ceil]
