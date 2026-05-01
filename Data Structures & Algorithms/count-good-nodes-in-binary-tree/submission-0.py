# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxs):
            if not root: 
                return 0
            res=0
            if root.val>=maxs:
                res=res+1
            maxs=max(root.val,maxs)
            res+=dfs(root.left,maxs)
            res+=dfs(root.right,maxs)
            return res
        
        
        return dfs(root,root.val)
        


        