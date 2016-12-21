class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # O(logk!) = O(klogk) time, O(k) space
        import heapq
        heap = []
        pairs = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i]+nums2[j], i, j])
        push(0, 0)
        while heap and len(pairs) < k:
            pairsum, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return pairs