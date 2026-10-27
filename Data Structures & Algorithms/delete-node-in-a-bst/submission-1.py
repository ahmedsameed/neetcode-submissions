# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(root,key1):

            if not root:
                return None
            if root.val<key1:
                root.right = dfs(root.right,key1)
            
            elif root.val>key1:
                root.left=dfs(root.left,key1)
            
            else:
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left
                
                else:
                    successor=root.right

                    while successor.left:
                        successor=successor.left

                    root.val=successor.val
                    key1=successor.val

                    root.right=dfs(root.right,key1)
            return root
        return dfs(root,key)


                



            
            
