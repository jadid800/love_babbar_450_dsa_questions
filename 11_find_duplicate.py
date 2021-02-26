import numpy as np
class Array_operation:
    def __init__(self, array):
        self.arr=array
        
        
    def find_dup_on2(self):
        for i in range(len(self.arr)):
            for j in range(i+1, len(self.arr)):
                if(self.arr[i]==self.arr[j]):
                    return self.arr[j]
    def find_dup_on1(self):
        another_arr= np.array([0]*len(self.arr))
        for i in self.arr:
            another_arr[i]+=1
            if(another_arr[i]==2):
                return i
        

array_operation=Array_operation(np.array(list(map(int, input().split()))))
print(array_operation.find_dup_on1())
