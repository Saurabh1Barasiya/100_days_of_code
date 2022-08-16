# Valid parinthesis check.

from collections import deque
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


def push_bottom(stack,element):
    ''' this function will push element at bottom of the stack. '''
    
    if stack.is_empty():
        stack.push(element)
        return
    else:
        num = stack.peek()
        stack.pop()
        push_bottom(stack,element)
        stack.push(num)

if __name__ == '__main__':
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.container)
    ele = 6
    push_bottom(stack,ele)
    print(stack.container)
  