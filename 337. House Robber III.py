# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs(root)[0]: maximum money robbed with or without robbing root
        # dfs(root)[1]: maximum money robbed without robbing root
        return self.dfs(root)[0]
        
    def dfs(self, root):
        if not root:
            return (0, 0)
        dfs_left = self.dfs(root.left)
        dfs_right = self.dfs(root.right)
        return (max(root.val+dfs_left[1]+dfs_right[1], dfs_left[0]+dfs_right[0]), dfs_left[0]+dfs_right[0])