class Solution:
    def addTwoLists(self, first, second):
        temp= first
        numbers=""
        while(temp):
            numbers+=str(temp.data)
            temp=temp.next
        number1 = int(numbers)
        temp= second
        numbers=""
        while(temp):
            numbers+=str(temp.data)
            temp=temp.next
        number = [x+" " for x in str(number1+int(numbers))]  
        numbers = "".join(number)
        return Node(numbers)
        
