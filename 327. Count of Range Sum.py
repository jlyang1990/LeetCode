class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # O(nlogn) time
        cumsum = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            cumsum[i] = cumsum[i-1] + nums[i-1]
        return self.countSort(cumsum, 0, len(cumsum), lower, upper)
        
        
    def countSort(self, cumsum, left, right, lower, upper):
        if right - left <= 1:
            return 0
        mid = (left+right)/2
        count = self.countSort(cumsum, left, mid, lower, upper) + self.countSort(cumsum, mid, right, lower, upper)  # here cumsum[left:mid] and cumsum[mid:right] are already sorted
        i, j = mid, mid
        for cumsumL in cumsum[left:mid]:
            while i < right and cumsum[i] - cumsumL < lower:  # one pass of cumsum[mid:right]
                i += 1
            while j < right and cumsum[j] - cumsumL <= upper:  # one pass of cumsum[mid:right]
                j += 1
            count += j - i
        cumsum[left:right] = sorted(cumsum[left:right])  # sorted function uses linear time to recognize and merge the already sorted halves
        return count