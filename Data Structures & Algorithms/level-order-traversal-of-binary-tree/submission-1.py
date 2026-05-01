# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        que=deque()
        que.append(root)

        while que:
            l=len(que)
            level=[]
            for i in range(l):
                node=que.popleft()
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)  
            if level:
                res.append(level)
                print(level)
        return res


            

        