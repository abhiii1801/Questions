class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(list(set(nums)))

        dic = {}

        for el in nums:
            if el in dic:
                return True
            else:
                dic[el]=1

        return False


