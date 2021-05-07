def find(arr, length, target):
  occurence= binarySearch(arr,0,length-1, target)
  if(occurence==-1):
    return[-1,-1]
  return [findFirst(arr, occurence, target), findLast(arr,occurence,target,length)]

def findFirst(arr, occurence, target):
  first= occurence
  while(first!=0 and arr[first-1]==target):
    first-=1
  return first
def findLast(arr, occurence, target, length):
  first= occurence
  while(first!=length-1 and arr[first+1]==target):
    first+=1
  return first



def binarySearch(arr,  left, right, target):
  
  while(left<=right):
    mid = (left+ right)//2
    if(arr[mid]==target):
      return mid
    elif(arr[mid]>target):
      right= mid-1
    else:
      left= mid+1
  return -1;
