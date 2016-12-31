# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        # method 1: recursive
        if not root:
            return []
        else:
            return  self.preorderTraversal(root.left) + self.preorderTraversal(root.right) + [root.val]
        '''
        
        # method 2: iterative
        result = []
        stack = []
        p = root
        while len(stack) > 0 or p:
            if p:
                result.insert(0, p.val)
                stack.append(p)
                p = p.right
            else:
                p = stack.pop()
                p = p.left
        return result