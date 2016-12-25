class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = {}
        for ticket in tickets:
            if ticket[0] not in targets:
                targets[ticket[0]] = [ticket[1]]
            else:
                targets[ticket[0]].append(ticket[1])
        for target in targets:
            targets[target].sort(reverse=True)
        result = []
        self.findItineraryHelper(targets, "JFK", result)
        return result[::-1]
        
    def findItineraryHelper(self, targets, target, result):
        while target in targets and targets[target]:
            self.findItineraryHelper(targets, targets[target].pop(), result)
        result.append(target)