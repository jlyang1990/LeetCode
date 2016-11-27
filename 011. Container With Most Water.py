class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # denote c(i,j) as area from i to j (we start from c(1,n))
        # suppose ai < aj, then c(i,j) > c(i,k), k = i+1, ..., j-1
        # thus the next step is to explore c(i+1, j)
        # at step c(i,j), (j-1)-(i+1)+1=j-i-1 areas are automatically excluded
        # total number of areas excluded = (n-1-1)+...+1 = (n-1)(n-2)/2
        # thus only n(n-1)/2 - (n-1)(n-2)/2 = n-1 areas need to be compared
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left]*(right-left))
                left += 1
            else:
                max_area = max(max_area, height[right]*(right-left))
                right -= 1
        return max_area