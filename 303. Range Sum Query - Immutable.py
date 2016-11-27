class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # O(n) space
        self.cumsum = nums
        for i in range(1, len(nums)):
            self.cumsum[i] += self.cumsum[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # O(1) query
        if i == 0:
            return self.cumsum[j]
        return self.cumsum[j] - self.cumsum[i-1]
        

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)