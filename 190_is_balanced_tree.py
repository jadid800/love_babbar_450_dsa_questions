def isBalanced(root):
    if(not root):
        return True
    return   ( abs ( length_of_tree(root.left) - length_of_tree(root.right) )<2  )  and isBalanced(root.left) and isBalanced(root.right)
    
def length_of_tree(root):
    if(not root):
        return 0
    return max( length_of_tree(root.left ) , length_of_tree(root.right) ) +1
        
