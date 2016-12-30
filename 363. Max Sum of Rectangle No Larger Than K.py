class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        maxSum = float("-inf")
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += matrix[i-1][j]
        for j in range(1, n):
            for i in range(m):
                matrix[i][j] += matrix[i][j-1]
        if m >= n:  # O(n^2mlogm) time
            for j in range(n):
                cumsum = [0]+[matrix[i][j] for i in range(m)]
                maxSum = max(maxSum, self.maxSumSort(cumsum, k, 0, m+1))
                for t in range(j):
                    cumsum = [0]+[matrix[i][j]-matrix[i][t] for i in range(m)]
                    maxSum = max(maxSum, self.maxSumSort(cumsum, k, 0, m+1))
        else:  # O(m^2nlogn) time
            for i in range(m):
                cumsum = [0]+[matrix[i][j] for j in range(n)]
                maxSum = max(maxSum, self.maxSumSort(cumsum, k, 0, n+1))
                for t in range(i):
                    cumsum = [0]+[matrix[i][j]-matrix[t][j] for j in range(n)]
                    maxSum = max(maxSum, self.maxSumSort(cumsum, k, 0, n+1))
        return maxSum
        
        
    def maxSumSort(self, cumsum, k, left, right):
        if right - left <= 1:
            return float("-inf")
        mid = (left+right)/2
        maxSum = max(self.maxSumSort(cumsum, k, left, mid), self.maxSumSort(cumsum, k, mid, right))
        j = mid
        for cumsumL in cumsum[left:mid]:
            while j < right and cumsum[j] - cumsumL <= k:
                j += 1
            if j > mid:
                maxSum = max(maxSum, cumsum[j-1] - cumsumL)
            if j == right:
                break
        cumsum[left:right] = sorted(cumsum[left:right])
        return maxSum