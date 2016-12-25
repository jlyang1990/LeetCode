# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [float("-inf")]
        self.maxPathSumHelper(root, result)
        return result[0]
        
        
    def maxPathSumHelper(self, root, result):
        if not root:
            return 0
        leftSum = self.maxPathSumHelper(root.left, result)
        rightSum = self.maxPathSumHelper(root.right, result)
        maxSinglePath = max(root.val, root.val+leftSum, root.val+rightSum)
        maxPath = max(maxSinglePath, root.val+leftSum+rightSum)
        result[0] = max(result[0], maxPath)
        return maxSinglePath