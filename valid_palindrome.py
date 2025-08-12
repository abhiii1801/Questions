#https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _recc(s, front, back):
            if front >= back:
                return True
            if s[front] != s[back]:
                return False
            return _recc(s, front + 1, back - 1)

        s = s.replace(" ", "")                  
        s = s.lower()                           
        s = "".join([x for x in s if x.isalnum()])
        return _recc(s, 0, len(s) - 1)
