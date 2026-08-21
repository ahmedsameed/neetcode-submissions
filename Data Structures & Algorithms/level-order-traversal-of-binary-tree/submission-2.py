# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()

        if root:
            q.append(root)
        res=[]
        while q:
            list=[]
            for i in range(len(q)):
                p=q.popleft()
                list.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            res.append(list)

        return res

        
        