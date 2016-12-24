class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        geneQueue = []
        self.nextMutation(start, bank, geneQueue)
        count = 1
        while geneQueue:
            tempQueue = []
            while geneQueue:
                gene = geneQueue.pop()
                if gene == end:
                    return count
                self.nextMutation(gene, bank, tempQueue)
            geneQueue = tempQueue
            count += 1
        return -1
        
        
    def nextMutation(self, gene, bank, queue):
        for i in range(8):
            for s in ["A", "C", "G", "T"]:
                new_gene = gene[:i]+s+gene[i+1:]
                if new_gene in bank:
                    queue.append(new_gene)
                    bank.remove(new_gene)