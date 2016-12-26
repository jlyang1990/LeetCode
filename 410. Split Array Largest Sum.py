class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # O(log(sum(nums)-max(nums))*n)
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left+right)/2
            if not self.validSplit(nums, m, mid):  # mid is too small to have valid split
                left = mid+1
            else:  # mid is large enough to have valid split but it can still be optimized
                right = mid-1
        return left
        
        
    def validSplit(self, nums, m, largest):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > largest:
                count += 1
                total = num
            if count > m:
                return False
        return True