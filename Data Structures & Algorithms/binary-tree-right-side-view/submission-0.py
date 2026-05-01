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

        while que:
            l=len(que)
            
            for i in range (l):
                    
                    node=que.popleft()
                    
                    if node:
                        print("Node")
                        print(node.val)
                        print("L")
                        print(l)
                        
                        if i==l-1:
                            print("i")
                            print(i)
                            print("L25")
                            print(node.val)
                            res.append(node.val)
                            if node.left:
                                que.append(node.left)
                            if node.right:
                                que.append(node.right)

                            
                        else:    
                            if node.left:
                                que.append(node.left)
                            if node.right:
                                que.append(node.right)

        return res

                



        