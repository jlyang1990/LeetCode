# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # bfs to ensure top-bottom direction
        if not root:
            return []
        resultL, resultR, resultM = [], [], []
        import Queue
        nodeQueue = Queue.Queue()
        nodeQueue.put((root, 0))
        while nodeQueue.qsize() > 0:
            node, level = nodeQueue.get()
            if node:
                if level < 0:
                    if len(resultL) < -level:
                        resultL.append([node.val])
                    else:
                        resultL[-level-1].append(node.val)
                if level > 0:
                    if len(resultR) < level:
                        resultR.append([node.val])
                    else:
                        resultR[level-1].append(node.val)
                if level == 0:
                    resultM.append(node.val)
                nodeQueue.put((node.left, level-1))
                nodeQueue.put((node.right, level+1))
        return resultL[::-1] + [resultM] + resultR