# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right, root):
            if not root:
                return True
            if left >= root.val or right <=root.val:
                return False
            return dfs (left,root.val,root.left) and dfs(root.val, right, root.right)
        
        return dfs(-1000000000,1000000000,root)
        