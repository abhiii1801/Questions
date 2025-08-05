#https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        current = 4
        def powertwo(n:int):
            nonlocal current
            if n<current:
                return False

            if n == current:
                return True
            
            current = 4*current
            return powertwo(n)

        if n==1:
            return True
        ans = powertwo(n)

        return ans