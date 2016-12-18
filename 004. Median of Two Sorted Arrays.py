class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.findMedianSortedArraysHelper(nums1, nums2, l/2+1)
        else:
            return (self.findMedianSortedArraysHelper(nums1, nums2, l/2)\
            +self.findMedianSortedArraysHelper(nums1, nums2, l/2+1))/2.0
        
    
    # find kth smallest element in nums1 and nums2
    # O(logk) time
    def findMedianSortedArraysHelper(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        # if nums1[i-1] < nums2[j-1], there are >= len(nums1)-i+len(nums2)-j+1 
        # = len(nums1)-min(len(nums1), k/2)+len(nums2)-min(len(nums2), k/2)+1 
        # >= len(nums1)-k/2+len(nums2)-k/2+1 = len(nums1)+len(nums2)-k+1 elements larger than 
        # nums1[i-1], thus nums1[0] to nums1[i-1] must be smaller than kth smallest element
        i, j = min(len(nums1), k/2), min(len(nums2), k/2)
        if nums1[i-1] < nums2[j-1]:
            return self.findMedianSortedArraysHelper(nums1[i:], nums2, k-i)
        else:
            return self.findMedianSortedArraysHelper(nums1, nums2[j:], k-j)