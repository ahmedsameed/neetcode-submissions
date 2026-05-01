# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        que=deque()
        que.append(root)
        if not root:
            return []
        while que:
            right=None
            l=len(que)
            
            for i in range (l):
                    
                    node=que.popleft()
                    
                    if node:
                        right=node
                        print("Node")
                        if node.left:
                                que.append(node.left)
                        if node.right:
                                que.append(node.right)
                        
            
            res.append(right.val)
        return res

                



        