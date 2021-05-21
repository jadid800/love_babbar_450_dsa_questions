from collections import deque 
def zigZagTraversal(root):
    label_result=[1]
    result=[]
    q= deque([root,0])
    
    while(q):
        
        v=q.popleft()
        label= q.popleft()
        if(label == label_result[0]):
            add_result(label_result,result)
        label_result.append(v.data)
        if(v.left != None):
            q.append(v.left)
            q.append(label+1)
        if(v.right != None):
            q.append(v.right)
            q.append(label+1)
    add_result(label_result,result)        
    return result        
            
def add_result(label_result, result):
    if( (label_result[0]+1)%2 == 1):
        for i in range(len(label_result)-1 , 0, -1):
            result.append(label_result[i])
        
    else:
        for i in range(1,len(label_result)):
            result.append(label_result[i])
    s= label_result[0]+1
    label_result[:]=[s]
            
