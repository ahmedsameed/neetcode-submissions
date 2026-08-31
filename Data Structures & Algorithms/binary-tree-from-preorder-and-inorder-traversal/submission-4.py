# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preindex=0
        mapi=defaultdict(int)
        for i in range(len(inorder)):
            mapi[inorder[i]]=i
        
        def dfs(l,r):
            if l>r:
                return 
            root=TreeNode(preorder[self.preindex])
            
            inorderindex=mapi[preorder[self.preindex]]
            self.preindex+=1
            root.left=dfs(l,inorderindex-1)
            root.right=dfs(inorderindex+1,r)
            return root
        return dfs(0,len(inorder)-1)