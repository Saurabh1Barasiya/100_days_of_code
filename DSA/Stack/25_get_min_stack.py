# get minimum element in stack.

# time complexity is O(1).
# space complexity is O(N).


# but is question ko hamko O(1) space complexity me solve karna h.



import sys
from collections import deque
class Stack:
    def __init__(self,maxsize):
        self.container = deque()
        self.maxsize = maxsize
        self.another_stack = deque()
        self.mini = sys.maxsize
    
    def push(self,val):
        if self.is_full():
            print("Stack is full")
            return
        self.container.append(val)
        self.mini = min(self.mini,self.peek())
        self.another_stack.append(self.mini)
        
    def pop(self):
        if self.is_empty():
           print("Stack is empty")
           return 
        self.container.pop()
        self.another_stack.pop()
    
    def get_min(self):
        if len(self.another_stack) == 0:
           print("Empty stack")
           return
        else:
            return self.another_stack[-1]
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def is_full(self):
        return len(self.container)==self.maxsize




stack = Stack(5)
stack.push(5)
# print(stack.get_min())
stack.push(3)
# print(stack.get_min())
stack.push(8)
# print(stack.get_min())
stack.push(2)
# print(stack.get_min())
stack.push(4)
# print(stack.get_min())

stack.pop()
stack.pop()
stack.pop()
stack.pop()
# stack.pop()
print(stack.get_min())
