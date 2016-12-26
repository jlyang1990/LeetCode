class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # f[k, i]: the max profit up until prices[i] (not included) using at most k transactions 
        # f[k, i] = max(f[k, i-1], f[k-1, j]-prices[j]+prices[i-1], 0<=j<=i-2) = max(f[k, i-1], prices[i-1]+max_{0<=j<=i-2}(f[k-1, j]-prices[j]))
        # f[0, i] = 0: 0 times transation makes 0 profit
        # f[k, 0] = f[k, 1] = 0: at most one price data point makes 0 profit
        # O(kn) time, O(n) space if k <= n//2; O(n) time, O(1) space if k > n//2
        n = len(prices)
        if k > n//2:  # the same as unlimited transactions
            profit = 0
            for i in range(1, n):
                profit += max(prices[i]-prices[i-1], 0)
            return profit
        profit = [0]*(n+1)
        for j in range(k):
            maxTemp = float("-inf")
            prepre, pre = 0, 0  # prepre records (previous) profit[i-2], pre records (previous) profit[i-1]
            for i in range(2, n+1):
                temp = profit[i]
                maxTemp = max(maxTemp, prepre-prices[i-2])
                profit[i] = max(profit[i-1], prices[i-1]+maxTemp)
                prepre, pre = pre, temp
        return profit[n]