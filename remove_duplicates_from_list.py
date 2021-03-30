def removeDuplicates(head):
    temp= head
    try:
        while(temp.next):
            while(temp.data == temp.next.data):
                temp.next = temp.next.next
                
            temp= temp.next
    except AttributeError:
        pass
    return head
