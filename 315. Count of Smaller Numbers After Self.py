class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(nlogn) time
        numsIndexCount = [[nums[i], i, 0] for i in range(len(nums))]  # [num, index, count]
        self.countSort(numsIndexCount, 0, len(nums))
        return [item[2] for item in sorted(numsIndexCount, key = lambda x: x[1])]
        
        
    def countSort(self, numsIndexCount, left, right):
        if right - left <= 1:
            return
        mid = (left+right)/2
        self.countSort(numsIndexCount, left, mid)
        self.countSort(numsIndexCount, mid, right)
        j = mid
        for i in range(left, mid):
            while j < right and numsIndexCount[j][0] < numsIndexCount[i][0]:
                j += 1
            numsIndexCount[i][2] += j - mid
        numsIndexCount[left:right] = sorted(numsIndexCount[left:right], key = lambda x: x[0])