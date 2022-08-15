class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = []
        self.top = -1
    
    def push(self,data):
        if self.is_full():
            print("Stack is Overflow")
            return
        else:
            self.top += 1
            self.stack.append(data)
    
    def show_data(self):
        for i in self.stack[::-1]:
            print(i)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            # element = self.stack[self.top]
            element = self.stack.pop()
            self.top -= 1
            return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty Underflow")
            return
        else:
            return self.stack[self.top]

    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False
    
    def is_full(self):
        if self.top == self.size-1:
            return True
        else:
            return False

stack = Stack(4)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
# stack.pop()
# stack.pop()
# # stack.pop()
# # stack.pop()
stack.show_data()




