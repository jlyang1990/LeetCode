class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy[i]: max_profit up to day i ending with buy (buy is not necessarily at day i)
        # sell[i]: max_profit up to day i ending with sell (sell is not necessarily at day i)
        # buy[i] = max{buy[i-1], sell[i-2]-prices[i]}
        # sell[i] = max{sell[i-1], buy[i-1]+prices[i]}
        if len(prices) == 0:
            return 0
        buy = -prices[0]
        sell = 0
        sell_prev = 0
        for i in range(1, len(prices)):
            buy, sell, sell_prev = max(buy, sell_prev-prices[i]), max(sell, buy+prices[i]), sell
        return sell