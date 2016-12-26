class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # For explanation, please see http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
        # O(n) time
        heights.append(0)
        stack = []
        maxArea = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = stack.pop()
                maxArea = max(maxArea, heights[h]*((i-stack[-1]-1) if stack else i))
        return maxArea