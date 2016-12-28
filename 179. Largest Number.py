class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        num.sort(cmp = lambda x, y: cmp(y+x, x+y))
        return str(int("".join(num)))  # use str(int()) to avoid nums = [0, 0]