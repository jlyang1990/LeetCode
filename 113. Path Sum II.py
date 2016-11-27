# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, sum, result, [])
        return result
        
    def dfs(self, root, sum, result, path):
        if root:
            if not root.left and not root.right and root.val == sum:
                result.append(path+[root.val])
            else:
                self.dfs(root.left, sum-root.val, result, path+[root.val])
                self.dfs(root.right, sum-root.val, result, path+[root.val])