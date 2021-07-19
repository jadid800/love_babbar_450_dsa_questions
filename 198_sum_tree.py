class Solution:
    def isSumTree(self,root):
        if(not root):
            return True
        if(not root.left and not root.right):
            return True
        if(root.data!= self.getSum(root.left) +self.getSum(root.right)):
            return False
            
        return self.isSumTree(root.left) and self.isSumTree(root.right)
        # Code here

    def getSum(self,root):
        if(not root):
            return 0
        return root.data+self.getSum(root.left)+ self.getSum(root.right)
        
            
