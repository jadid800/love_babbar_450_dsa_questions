def intersetPoint(head1,head2):
    set1= set([])
    temp1= head1
    while(temp1):
        set1.add(temp1)
        temp1= temp1.next
    temp2= head2
    while(temp2):
        if(temp2 in set1):
            return temp2.data
        temp2 = temp2.next
    return -1
