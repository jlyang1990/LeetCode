# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        self.longestConsecutiveHelper(root, result, 1)
        return result[0]
        
    
    def longestConsecutiveHelper(self, root, result, length):
        if root:
            if root.left and root.left.val == root.val+1:
                self.longestConsecutiveHelper(root.left, result, length+1)
            else:  # root.left = None or root.left.val != root.val+1
                result[0] = max(result[0], length)
                self.longestConsecutiveHelper(root.left, result, 1)
            if root.right and root.right.val == root.val+1:
                self.longestConsecutiveHelper(root.right, result, length+1)
            else:  # root.right = None or root.right.val != root.val+1
                result[0] = max(result[0], length)
                self.longestConsecutiveHelper(root.right, result, 1)