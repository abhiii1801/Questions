#https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def lcmAndGcd(self, a : int, b : int):
        # code here
        f = a
        s = b
        while (b != 0):
            temp = b
            b = a%b
            a = temp
        
        gcd = a
        lcm = (f * s)//gcd
        
        return [lcm, gcd]
