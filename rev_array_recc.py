#https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # front = 0
        # back = len(s) - 1
        # while front < back:
        #     temp = s[front]
        #     s[front] = s[back]
        #     s[back] = temp
        #     front+=1
        #     back-=1
        def reverseArr(s, start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            reverseArr(s, start + 1, end - 1)
        
        reverseArr(s,0,len(s)-1)

