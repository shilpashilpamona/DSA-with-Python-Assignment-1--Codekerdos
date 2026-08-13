class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None

        return self.top.data


stack = Stack()

stack.push(20)
stack.push(40)

print(stack.peek())  # 40
print(stack.pop())  # 40
print(stack.peek())  # 20
