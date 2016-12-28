# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.findLeavesHelper(root, result)
        return result
        
    
    def findLeavesHelper(self, root, result):
        if not root:
            return 0
        level = 1 + max(self.findLeavesHelper(root.left, result), self.findLeavesHelper(root.right, result))
        if len(result) < level:
            result.append([root.val])
        else:
            result[level-1].append(root.val)
        return level