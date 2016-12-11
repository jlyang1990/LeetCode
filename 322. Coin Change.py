class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dynamic programming
        # O(n*amount) time, O(amount) space
        number = [0]+[float("inf")]*amount
        for current_amount in range(1, amount+1):
            for coin in coins:
                if coin <= current_amount:
                    number[current_amount] = min(number[current_amount-coin]+1, number[current_amount])
        return number[amount] if number[amount] < float("inf") else -1