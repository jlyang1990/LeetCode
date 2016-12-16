class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # candidate1 has its pair set
        # candidate2 is different from candidate1 and is not in pair set of candidate1
        # candidate2 share the same pair set as candidate1
        # O(n) time, O(1) space
        count1, count2, candidate1, candidate2 = 0, 0, float("inf"), float("inf")
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                count1, candidate1 = 1, num
            elif count2 == 0:
                count2, candidate2 = 1, num
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
        return [(candidate1, candidate2)[i] for i in range(2) if (count1, count2)[i] > len(nums)/3]