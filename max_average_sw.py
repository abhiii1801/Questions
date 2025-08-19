#https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:

        current_sum = sum(arr[:k])
        current_avg = current_sum/k
        max_avg = current_avg

        for i in range(len(arr)-k):
            current_sum = current_sum - arr[i] + arr[i + k]
            current_avg = current_sum/k
            if current_avg > max_avg:
                max_avg = current_avg

        return max_avg




        