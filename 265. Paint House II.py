class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # O(nk) time, O(k) space
        if len(costs) == 0:
            return 0
        k = len(costs[0])
        if k == 1:
            if len(costs) == 1:
                return costs[0][0]
            else:
                return 0
        costK = [0]*k
        for cost in costs:
            minCostK, min2CostK = float("inf"), float("inf")
            for i in range(k):
                if costK[i] <= minCostK:
                    min2CostK, minCostK = minCostK, costK[i]
                elif costK[i] <= min2CostK:
                    min2CostK = costK[i]
            for i in range(k):
                costK[i] = minCostK + cost[i] if costK[i] != minCostK else min2CostK + cost[i]
        return min(costK)