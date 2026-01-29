class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        l_arr = [0] * n
        r_arr = [0] * n

        curr = 1
        for i in range(n):
            l_arr[i] = curr
            curr *= arr[i]

        curr = 1
        for i in range(n-1 ,-1, -1):
            r_arr[i] = curr * l_arr[i]
            curr *= arr[i]

        return r_arr

        
        


         
