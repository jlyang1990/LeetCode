# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        self.dfs(root, result, "")
        return result
        
    def dfs(self, root, result, string):
        if root:
            if root.left == None and root.right == None:
                result.append(string+str(root.val))
            else:
                self.dfs(root.left, result, string+str(root.val)+"->")
                self.dfs(root.right, result, string+str(root.val)+"->")