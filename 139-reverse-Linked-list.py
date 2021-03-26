
class Solution:
    #Function to reverse a linked list.
    def __init__(self):
        self.head= Node
    def reverseList(self, head):
        self.head= head
        prev= None
        temp= head
        next1= head.next
        while(next1):
          temp.next=prev
          prev=temp
          temp= next1
          next1 =next1.next
        temp.next= prev
        return temp



class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def prinList(head):
  temp= head
  while(temp):
    print(temp.data, end=" ")
    temp= temp.next
  print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        prinList(newHead)



