from collections import deque


class Stack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def is_Empty(self):
        return len(self.q1) == 0

    def enque(self, data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.is_Empty():
            return None
        else:
            return self.q1.popleft()

    def peek(self):
        if self.is_Empty():
            return None
        else:
            return self.q1[0]


stack = Stack()
stack.enque(10)
stack.enque(20)
stack.pop()
stack.peek()
