import numpy as np
class Array_operation:
    def __init__(self, array):
        self.arr=array
        
        
    def jump(self):
        i=0
        jumps=0
        try:
            while(i<len(self.arr)-1):
                i+=self.arr[i]
                jumps+=1
                if(self.arr[i] == 0):
                    return -1
            return jumps
        except IndexError :
            return jumps
        
        

array_operation=Array_operation(np.array(list(map(int, input().split()))))
print(array_operation.jump())
