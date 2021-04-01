def reverseDLL(head):
    temp= head
    while(temp):
        temp.next , temp.prev= temp.prev, temp.next
        if(not temp.prev):
            break
        temp= temp.prev
        
    return temp
