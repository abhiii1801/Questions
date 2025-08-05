#https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        sum = 0
        num = n
        while (n):
            dig = n % 10
            sum += dig**3
            n = n//10
        
        if num == sum:
            return True
        return False
        