# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        start,end = 0, len(arr) - 1

        while start<=end:
            mid = (start+end)//2
            if arr[mid] == target:
                return True

            if arr[start] == arr[end] == arr[mid]:
                start+=1
                end-=1
                continue

            if arr[start] <= arr[mid]: #left sorted
                if(arr[start]<=target<=arr[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if (arr[mid]<=target<=arr[end]):
                    start = mid + 1
                else:
                    end = mid - 1
        return False

        
        