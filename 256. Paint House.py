class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # costR[i]: minimum cost to paint until house i (exclusive) ending with red(0)
        # costB[i]: minimum cost to paint until house i (exclusive) ending with blue(1)
        # costG[i]: minimum cost to paint until house i (exclusive) ending with green(2)
        # costR[i] = min(costB[i-1], costG[i-1]) + costs[i][0]
        # costB[i] = min(costR[i-1], costG[i-1]) + costs[i][1]
        # costG[i] = min(costR[i-1], costB[i-1]) + costs[i][2]
        # costR[0] = costB[0] = costG[0] = 0
        # O(n) time, O(1) space
        costR, costB, costG = 0, 0, 0
        for cost in costs:
            costR, costB, costG = min(costB, costG) + cost[0], min(costR, costG) + cost[1], min(costR, costB) + cost[2]
        return min(costR, costB, costG)