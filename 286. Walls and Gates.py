class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # method 1: dfs
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)
        
    def dfs(self, rooms, i, j, distance):
        if i in [-1, len(rooms)] or j in [-1, len(rooms[0])] or rooms[i][j] < distance:
            return
        rooms[i][j] = distance
        self.dfs(rooms, i-1, j, distance+1)
        self.dfs(rooms, i+1, j, distance+1)
        self.dfs(rooms, i, j-1, distance+1)
        self.dfs(rooms, i, j+1, distance+1)
        
        
        # method 2: bfs
        import Queue
        roomsQueue = Queue.Queue()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    roomsQueue.put((i, j))
        while not roomsQueue.empty():
            i, j = roomsQueue.get()
            if i > 0 and rooms[i-1][j] == 2147483647:
                rooms[i-1][j] = rooms[i][j]+1
                roomsQueue.put((i-1, j))
            if i < len(rooms)-1 and rooms[i+1][j] == 2147483647:
                rooms[i+1][j] = rooms[i][j]+1
                roomsQueue.put((i+1, j))
            if j > 0 and rooms[i][j-1] == 2147483647:
                rooms[i][j-1] = rooms[i][j]+1
                roomsQueue.put((i, j-1))
            if j < len(rooms[0])-1 and rooms[i][j+1] == 2147483647:
                rooms[i][j+1] = rooms[i][j]+1
                roomsQueue.put((i, j+1))