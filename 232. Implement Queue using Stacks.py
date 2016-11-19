class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        temp_stack = []
        while len(self.queue) > 0:
            temp_stack.append(self.queue.pop())
        temp_stack.append(x)
        while len(temp_stack) > 0:
            self.queue.append(temp_stack.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[len(self.queue)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0