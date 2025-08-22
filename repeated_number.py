class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hashed = {}
        repeated = -1
        for i in A:
            if i in hashed:
                repeated = i
                hashed[i]+=1
            else:
                hashed[i] = 1
                
        missing = -1
                
        for j in range(1,len(A)+1):
            if j not in hashed:
                missing = j
                
        return repeated,missing
                
        
            
            
            
                    