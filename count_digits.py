#https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides(self, n):
        # code here
        og = n
        count = 0
        while(n):
            num = n%10
            if num != 0:
                if og % num == 0:
                    count+=1
            n = n // 10
        
        return count