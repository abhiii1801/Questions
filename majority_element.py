#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]

        # Moore’s Voting Algorithm
        # count = 0
        # cand = None
        # for num in nums:
        #     if count==0:
        #         cand = num
        #     if num == cand:
        #         count+=1
        #     else:
        #         count-=1
        
        # return cand
