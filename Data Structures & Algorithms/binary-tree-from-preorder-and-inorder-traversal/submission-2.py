# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapd=defaultdict(int)

        for i in range(len(inorder)):
            mapd[inorder[i]]=i
        

        preindex=0
        def dfs(l,r):
            if l>r:
                return 
            nonlocal preindex
            rootval=preorder[preindex]
            preindex=preindex+1
            root=TreeNode(rootval)
            mid=mapd[rootval]
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        return dfs(0,len(inorder)-1)
