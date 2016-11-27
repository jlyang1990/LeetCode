class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C-A)*(D-B) + (G-E)*(H-F)
        # potential overlapping area
        left = max(A, E)
        right = min(C, G)
        bottom = max(B, F)
        top = min(D, H)
        if left < right and bottom < top:
            area -= (right-left)*(top-bottom)
        return area