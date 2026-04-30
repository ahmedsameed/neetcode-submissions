# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #locl maxima 
         #global varibale 
        self.res=0
        #res=height of left + right
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.res=max(self.res,left+right)  # One we keep to reord at tht stage
            return 1+max(left,right)  # Another we keep to good deeper into the tree
        dfs(root)
        return self.res
        



