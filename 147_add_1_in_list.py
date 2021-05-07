class Solution:
    def addOne(self,head):
        temp= head
        numbers=""
        while(temp):
            numbers+=str(temp.data)
            temp=temp.next
        numbers = int(numbers)+1
        newNode= Node(numbers)
        head= newNode
        return head
