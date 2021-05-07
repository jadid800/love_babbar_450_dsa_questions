def findIntersection(head1,head2):
    set1= set([])
    temp= head1
    while(temp):
        set1.add(temp.data)
        temp = temp.next
    newNode = None
    prev=None
    temp = head2
    set2=set([])
    while(temp):
        if(temp.data in set1 and not  temp.data  in set2 ):
            set2.add(temp.data)
            if(not newNode):
                newNode = Node(temp.data)
                prev= newNode 
            else:
                prev.next = Node(temp.data)
                prev = prev.next
        temp= temp.next
    return newNode
                
