import numpy as np
class Array_operation:
    def __init__(self, array1, array2):
        self.array1=array1
        self.array2=array2
        
    def union(self):
        union_arr=self.__copy_element(array1)
        for i in array2:
            if(not self.__isin(array1,i) and not self.__isin(union_arr,i)):
                union_arr.append(i)
        return np.array(union_arr)
        
    def interset(self):
        intetset_arr=[]
        for i in array1:
            if(self.__isin(array2, i) and not self.__isin(intetset_arr,i)):
                intetset_arr.append(i)
        return np.array(intetset_arr)
        
    def __copy_element(self,  copy_from):
        copy_to=[]
        for i in copy_from:
            copy_to.append(i)
        return copy_to
        
    def __isin(self,array,target):
        for i in array:
            if(i==target):
                return True
        return False
        
array1=np.array(list(map(int, input().split())))
array2=np.array(list(map(int, input().split())))
array_operation=Array_operation(array1,array2)
print("union array: ",array_operation.union())
print("interset array: ", array_operation.interset())




