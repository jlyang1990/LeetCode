class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # O(n) time
        area = 0
        left, right = 0, len(height)-1
        maxleft, maxright = 0, 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    area += maxleft-height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    area += maxright-height[right]
                right -= 1
        return area