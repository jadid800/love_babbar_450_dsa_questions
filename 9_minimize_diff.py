import numpy as np
class Array_operation:
    def __init__(self, array):
        self.arr=array

    def minimize_diff(self,k):
        maximum=max(self.arr)-k #max, min function is very easy to build. so used built in function
        if(maximum<0):
            maximum+=k
        minimum = min(self.arr)+k
        return abs(min((maximum-minimum) ,(maximum-(minimum-k)) ))

array1=np.array(list(map(int, input().split())))

array_operation=Array_operation(array1)

print(array_operation.minimize_diff(int(input("k: "))))
