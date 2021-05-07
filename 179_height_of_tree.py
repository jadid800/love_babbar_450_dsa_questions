
class Solution:
    def height(self, root, label=0):
        if( not root):
            return label
        return max(self.height(root.left, label+1),self.height(root.right, label+1))
