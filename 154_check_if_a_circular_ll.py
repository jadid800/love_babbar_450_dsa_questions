def isCircular(head):
    temp= head.next
    while(temp):
        if(temp==head):
            return 1
    return 0
