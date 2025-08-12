#https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = len(nums) - 1

        while one <= two:
            if nums[one] == 2:
                nums[two], nums[one] = nums[one], nums[two]
                two-=1
            elif nums[one] == 1:
                one+=1
            elif nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                one+=1
                zero+=1
                

