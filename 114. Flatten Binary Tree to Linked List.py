# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # method 1
        self.flattenHelper(root)
        
        
    def flattenHelper(self, root):
        if root:
            if not (root.left or root.right):
                return root
            if not root.right:
                left_end = self.flattenHelper(root.left)
                root.right = root.left
                root.left = None
                return left_end
            if not root.left:
                right_end = self.flattenHelper(root.right)
                return right_end
            left_end = self.flattenHelper(root.left)
            right_end = self.flattenHelper(root.right)
            left_end.right = root.right
            root.right = root.left
            root.left = None
            return right_end

        
        # method 2
        if root:
            if not root.left:
                self.flatten(root.right)
            else:
                self.flatten(root.left)
                self.flatten(root.right)
                left_end = root.left
                while left_end.right:
                    left_end = left_end.right
                left_end.right = root.right
                root.right = root.left
                root.left = None