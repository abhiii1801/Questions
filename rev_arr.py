arr = [3, 6, 2, 7, 9]
start = 0
end = len(arr) - 1

while start<end:
    front = arr[start]
    arr[start] = arr[end]
    arr[end] = front
    start +=1
    end-=1
    
print(arr)