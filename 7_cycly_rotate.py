import numpy as np
class Array_operation:
    def __init__(self, array):
        self.arr=array
        
    def rorate_in_another(self):
        new_arr=[]
        new_arr.append(self.arr[len(self.arr)-1])
        for i in range(1, len(self.arr)):
            new_arr.append(i)
            
        return np.array(new_arr)
    def rtate_in_arr(self):
        last_element=self.arr[len(self.arr)-1]
        for i in range(len(self.arr)-1, 0,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[0]=last_element
        
    
        
array1=np.array(list(map(int, input().split())))

array_operation=Array_operation(array1)
array_operation.rtate_in_arr()
print(array_operation.arr)




