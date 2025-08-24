#https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

class Solution:    
    def printNos(self,n):
        #Code here
        def _print(num,curr):
            if curr <= num:
                print(curr, end=" ")
                _print(num, curr + 1)

        _print(n,1)
            
#https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/
            
class Solution:
    def printNos(self, n):
        # Code here
        def _print(n,curr):
            if curr > 0:
                print(curr, end=" ")
                _print(n,curr-1)
                
        _print(n,n)