from collections import deque
# stack = deque()

class Stack:
    def __init__(self,maxsize):
        self.container = deque()
        self.maxsize = maxsize
    
    def push(self,val):
        if self.is_full():
            raise Exception("Stack is full")
        self.container.append(val)
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.container.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def is_full(self):
        return len(self.container)==self.maxsize

stack = Stack(4)    
# print(stack.is_full())   # False
# abhi stack full nahi h.


# stack.push(10)  
# stack.push(20)
# stack.push(30)
# stack.push(40)
# print(stack.is_full())  # True


# print(stack.peek()) # 40.

# stack.pop()  # remove 1 element from stack.
# print(stack.peek()) # 30.

# print(stack.is_empty())

# print(stack.size())

# stack.pop()
# stack.pop()
# stack.pop()
# print(stack.is_empty())
# print(stack.size())
# stack.peek()
# print(stack.size())
# stack.push(50)
# stack.push(50)
# stack.push(50)
# stack.push(50)
# stack.push(50)


# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

print(stack.size())
print(stack.is_empty())
print(stack.is_full())
# print(stack.peek())
stack.push(10)
print(stack.peek())


