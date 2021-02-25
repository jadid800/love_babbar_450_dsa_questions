import numpy as np
#2 2 1 0 2
class Array_operation:
    def __init__(self,array):
        self.array=array
        
    def sort_arr(self):
        i=0
        add_num=[0,0,0]
        for number in range(3):
            add_num[number]=self.count_num(number)
        add_val=0
        for j in range(3):
            
            for k in range(add_num[j]):
                self.array[i]=add_val
                i+=1
            add_val+=1
            
            
    def count_num(self, n): #because count is a built in function
        repeatation=0
        for l in range(0,len(self.array)):
           
            
            if(self.array[l]==n):
                
                repeatation+=1
        
        return repeatation
        
        
        
arr=np.array(list(map(int, input().split())))
array_cls= Array_operation(arr)  
array_cls.sort_arr()

print(arr)

