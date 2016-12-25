class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # since (w, h1) cannot be contained in (w, h2) if h1 < h2, we need to put (w, h2) in front of (w, h1)
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        tails = [0]*len(envelopes)
        size = 0
        for x in envelopes:
            left, right = 0, size-1
            while left <= right:
                mid = (left+right)//2
                if tails[mid] < x[1]:
                    left = mid+1
                else:
                    right = mid-1
            tails[left] = x[1]
            size = max(size, left+1)
        return size