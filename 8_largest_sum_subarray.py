import numpy as np
class Array_operation:
    def __init__(self, array):
        self.arr=array
        
    def largest_sum(self):
        max_sum=self.arr[0]
        summation=self.arr[0]
        for i in range(1, len(self.arr)):
            summation+= self.arr[i]
            if(summation>max_sum):
                max_sum=summation
        return max_sum
        
        
    
        
array1=np.array(list(map(int, input().split())))

array_operation=Array_operation(array1)

print(array_operation.largest_sum())




