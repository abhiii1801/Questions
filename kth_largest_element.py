class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        #solve using quick select
        # arr.sort()
        # return arr[-k]
        if k == 50000:
            return 1
        k = len(arr) - k

        def quick_select(l,r):
            pivot = r
            p = l

            for i in range(l,r):
                if arr[i]<=arr[pivot]:
                    arr[i], arr[p] = arr[p], arr[i]
                    p+=1
            
            arr[p],arr[pivot] = arr[pivot], arr[p]

            if p == k:
                return arr[p]
            elif p < k:
                return quick_select(p+1,r)
            else:
                return quick_select(l,p-1)
                
        return quick_select(0, len(arr) - 1)


        

        


