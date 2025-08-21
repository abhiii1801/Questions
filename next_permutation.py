class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pivot = -1

        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i
                break

        if pivot==-1:
            arr.sort()
            return
        
        for i in range(len(arr)-1,0,-1):
            if arr[i] > arr[pivot]:
                a = arr[i]
                arr[i] = arr[pivot]
                arr[pivot] = a
                break

        i = pivot+1
        j = len(arr) - 1
        while i<j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1



        