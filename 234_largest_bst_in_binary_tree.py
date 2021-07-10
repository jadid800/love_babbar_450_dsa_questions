def largestBst(root):
    if(not root):
        return 0
    if(isBSTUtil(root)):
        return getfullCount(root)
    return max(largestBst(root.right),largestBst(root.left) )
    
    
    
    
def getfullCount(root):
 
    if (root == None):
        return 0
     
    return 1+getfullCount(root.right)+getfullCount(root.left)
    
def isBSTUtil(node, mini= -4294967296, maxi= 4294967296):
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))
