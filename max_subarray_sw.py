#https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        current_sum = sum(arr[:k])
        max_sum = current_sum
        
        for i in range(len(arr) - k):
            current_sum = current_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, current_sum)
            
        return max_sum
        
        