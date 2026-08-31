class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, data):
        self.items.append(data)
        print("Data append in the array list :", data)

    def pop_item(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.items.pop()
            print("Item poppped")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.items[-1])


stack = Stack()

stack.add_item(20)
stack.add_item(30)
stack.add_item(60)
stack.add_item(630)
stack.pop_item()
stack.peek()
