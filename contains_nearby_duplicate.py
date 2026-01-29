class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = set()
        if k > n:
            return n != len(set(nums))

        for i in range(k):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        
        for i in range(n-k):
            if nums[i+k] in s:
                return True
            else:
                s.add(nums[i+k])

            s.remove(nums[i])

        return False


        

        


