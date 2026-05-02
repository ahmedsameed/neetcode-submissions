# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        que=deque()
        res=[]
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            que.append(root.val)
            dfs(root.right)
        dfs(root)
        
        while k>0:
            result=que.popleft()
            k=k-1
        return result
            
        