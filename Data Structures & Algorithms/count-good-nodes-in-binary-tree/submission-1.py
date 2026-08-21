# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root,maxi):
            k=0
            if not root:
                return 
            if maxi<=root.val:
                maxi=root.val
                nonlocal res
                res=res+1
            dfs(root.right,maxi)
            dfs(root.left,maxi)

        dfs(root,root.val)

        return res
            


        