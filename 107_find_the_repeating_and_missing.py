class Solution:
    def findTwoElement(self,arr, n): 
        trackArr= [0]*n
        resultarr = [0,0]
        for i in arr:
            trackArr[i-1]+=1
        
        
        for i in range(n):
            if(trackArr[i]==2):
                resultarr[0]=i+1
            elif(trackArr[i]==0):
                resultarr[1]=i+1
                
        return resultarr
