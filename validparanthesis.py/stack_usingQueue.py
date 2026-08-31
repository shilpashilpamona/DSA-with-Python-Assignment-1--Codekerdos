from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def _isEmpty(self):
        return len(self.q1) == 0

    def push(self, data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.popleft)


stack = Stack()
stack.push(10)
stack.push(20)
