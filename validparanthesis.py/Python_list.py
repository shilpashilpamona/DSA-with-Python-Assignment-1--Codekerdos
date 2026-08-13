class Stack:

    def __init__(self):
        self.item = []

    def _isEmpty(self):
        return len(self.item) == 0

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if self._isEmpty():
            return None
        else:
            print("item popped", self.item.pop())

    def peek(self):
        if self._isEmpty():
            return True
        else:
            print("item peeked", self.item[-1])


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()
stack.peek()
