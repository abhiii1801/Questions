#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False

        x = str(x)

        front = 0
        back = len(x) - 1

        while (front < back):
            if x[front] != x[back]:
                return False
            front+=1
            back-=1
        
        return True
