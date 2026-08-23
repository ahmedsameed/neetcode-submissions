# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            if not root:
                return 0
            lefttree=dfs(root.left)
            righttree=dfs(root.right)
            nonlocal res
            res=max(res,righttree+lefttree)

            return 1+max(lefttree, righttree)

        dfs(root)
        return res