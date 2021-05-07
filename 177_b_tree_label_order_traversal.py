import collections
class Solution:
    def levelOrder(self,root ):
        q = collections.deque([root])
        result = []
        while( q):
            vert= q.popleft()
            result.append(vert.data)
            if(vert.left):
                q.append(vert.left)
                
            if(vert.right):
                q.append(vert.right)  
        return result
