# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHelper(root)[0]
    
    # record depth during recursion to avoid double recursion (one for depth and another for balance)    
    def isBalancedHelper(self, root):
        if not root:
            return True, 0
        judge_left, depth_left = self.isBalancedHelper(root.left)
        judge_right, depth_right = self.isBalancedHelper(root.right)
        judge = judge_left and judge_right and (abs(depth_left - depth_right) <= 1)
        depth = 1 + max(depth_left, depth_right)
        return judge, depth