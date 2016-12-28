class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # transform edges to edgeDic to reduce time costs in dfs
        edgeDic = [[] for i in range(n)]
        for edge in edges:
            edgeDic[edge[0]].append(edge[1])
            edgeDic[edge[1]].append(edge[0]) 
        visited = [False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(n, edgeDic, visited, i)
                count += 1
        return count
        
    def dfs(self, n, edgeDic, visited, i):
        visited[i] = True
        for j in edgeDic[i]:
            if not visited[j]:
                self.dfs(n, edgeDic, visited, j)