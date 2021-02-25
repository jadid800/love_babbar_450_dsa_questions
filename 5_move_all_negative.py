    def bubble_sort(self):
        for i in range(len(self.arr)):
            for j in range(i+1, len(self.arr)):
                if(arr[i]>arr[j]):
                    arr[i],arr[j]=arr[j],arr[i]
