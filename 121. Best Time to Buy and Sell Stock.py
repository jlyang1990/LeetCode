class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method 1
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit
        
        # method 2
        # construct list of price differences
        # max_profit = maximum consecutive sum, dynamic programming
        profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, 0) + prices[i] - prices[i-1]
            max_profit = max(max_profit, profit)
        return max_profit