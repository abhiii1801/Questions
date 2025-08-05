#https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        current = 3
        def powertwo(n:int):
            nonlocal current
            if n<current:
                return False

            if n == current:
                return True
            
            current = 3*current
            return powertwo(n)

        if n==1:
            return True
        ans = powertwo(n)

        return ans