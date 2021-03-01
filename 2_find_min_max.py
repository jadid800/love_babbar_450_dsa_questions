import numpy as np
class array_class:
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

arr= np.array(list(map(int, input().split())))

print("min",array_class(arr).get_min())
print("max",array_class(arr).get_max())

