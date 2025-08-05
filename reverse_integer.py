#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0 :
            neg = True
            x = abs(x)

        rev = 0
        while(x):
            rev = (rev *10) + (x%10)
            x = x //10

        if neg:
            rev =  0 - rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev