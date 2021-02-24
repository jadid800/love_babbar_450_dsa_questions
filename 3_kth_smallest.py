import numpy as np
class Array_class:
    def __init__(self,arr):
        self.arr=arr
        self.__min=arr[0]
        self.__max=arr[0]
    def get_min(self):
        for i in arr:
            if(i<self.__min):
                self.__min=i
        return self.__min
        
    def get_max(self):
        for i in arr:
            if(i>self.__max):
                self.__max=i
        return self.__max
    def kth_min(self,k):
        self.__bubble_sort()
        return arr[k-1]
    def __bubble_sort(self):
        for i in range(len(self.arr)):
            for j in range(i+1, len(self.arr)):
                if(arr[i]>arr[j]):
                    arr[i],arr[j]=arr[j],arr[i]
                
        
        

arr= np.array(list(map(int, input("give array ").split())))
k=int(input("input k "))
arr_class_inst= Array_class(arr)
print(arr_class_inst.kth_min(k))

