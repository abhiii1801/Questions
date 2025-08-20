#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(len(arr) - M+1):
            curr_diff = arr[i+M-1] - arr[i] 
            min_diff = min(curr_diff, min_diff)
            
        return min_diff
        