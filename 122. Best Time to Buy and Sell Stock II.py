class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method 1
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i]-prices[i-1], 0)
        return max_profit

        # method 2: dp
        # buy[i]: max_profit up to day i ending with buy (buy is not necessarily at day i)
        # sell[i]: max_profit up to day i ending with sell (sell is not necessarily at day i)
        # buy[i] = max{buy[i-1], sell[i-1]-prices[i]}
        # sell[i] = max{sell[i-1], buy[i-1]+prices[i]}
        if len(prices) == 0:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy, sell = max(buy, sell-prices[i]), max(sell, buy+prices[i])
        return sell