class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # s = set()
        # for n in nums:
        #     if n in s:
        #         return n
        #     s.add(n)

        #floyd cycle detection

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

