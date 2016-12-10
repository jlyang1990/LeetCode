# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution, using idea of dfs
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersHelper(root, 0)
        
    def sumNumbersHelper(self, root, number):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return number*10+root.val
        else:
            return self.sumNumbersHelper(root.left, number*10+root.val) + self.sumNumbersHelper(root.right, number*10+root.val)