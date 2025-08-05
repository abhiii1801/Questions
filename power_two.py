#https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        current = 2
        def powertwo(n:int):
            nonlocal current
            if n<current:
                return False

            if n == current:
                return True
            
            current = 2*current
            return powertwo(n)

        if n==1:
            return True
        ans = powertwo(n)

        return ans

