#https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

class Solution:
    def frequencyCount(self, arr):
        #  code here
        count = {x : 0 for x in range(1,len(arr)+1)}
        
        for i in arr:
            count[i]+=1

        return list(count.values())
        

