import collections
def reverseLevelOrder(root):
    q = collections.deque([root])
    result = []
    while(q):
        vert= q.popleft()
        if(vert.right):
            q.append(vert.right)  
        result.append(vert.data)
        if(vert.left):
            q.append(vert.left)
    result.reverse()
    
            
    return result
