# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is a univalue subtree, then:
        # 1. root.left is None or root.left is a univalue subtree and root.left.val = root.val
        # 2. root.right is None or root.right is a univalue subtree and root.right.val = root.val
        count = [0]
        self.countHelper(root, count)
        return count[0]
        
    
    def countHelper(self, root, count):
        if not root:
            return True
        left = self.countHelper(root.left, count)
        right = self.countHelper(root.right, count)
        if left and right:
            if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
                return False
            count[0] += 1
            return True
        return False