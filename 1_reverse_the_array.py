def reverse_arr(arr):
    for i in range((len(arr)-1)//2):
        arr[i],arr[len(arr)-1-i]= arr[len(arr)-1-i], arr[i]
        
import numpy as np
arr= np.array(list(map(int, input().split())))
reverse_arr(arr)
print(arr)

