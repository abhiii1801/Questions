#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = [[i,val] for i,val in enumerate(nums)]
        nums2.sort(key= lambda x : x[1])
        start = 0
        end = len(nums2) - 1
        for i in range(end):
            if (nums2[start][1] + nums2[end][1]) == target:
                return [nums2[start][0], nums2[end][0]]
            elif (nums2[start][1] + nums2[end][1]) > target:
                end -= 1
            else:
                start += 1