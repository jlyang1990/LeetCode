# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.rightSideViewHelper(root, result, 1)
        return result
        
    # modified preorder traversal
    def rightSideViewHelper(self, root, result, level):
        if root:
            if len(result) < level:
                result.append(root.val)
            self.rightSideViewHelper(root.right, result, level+1)
            self.rightSideViewHelper(root.left, result, level+1)