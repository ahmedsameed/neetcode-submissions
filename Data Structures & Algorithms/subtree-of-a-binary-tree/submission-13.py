class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if isSameTree(root, subRoot):  # match found at this node
            return True

        # always check children regardless of value match
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)