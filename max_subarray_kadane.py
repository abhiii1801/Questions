class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        # for i,_ in enumerate(nums):
        #     curr_sum = 0
        #     for j in nums[i:]:
        #         curr_sum += j
        #         max_sum = max(max_sum, curr_sum)

        # return max_sum

        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if curr_sum <0:
                curr_sum = 0

        return max_sum