class Node:
    def __init__(self, data):
        self.Node = data
        self.next = None

class Stack():

    def __init(self):
        self.top = None

    def _isEmpty(self):
        return self.top is None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def     
