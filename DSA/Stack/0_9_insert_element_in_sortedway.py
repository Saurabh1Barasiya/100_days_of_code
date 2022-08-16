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

def insert_sorted_order(stack,element):
    if stack.is_empty() or  stack.peek() < element  :
        stack.push(element)
        return
    else:
        num = stack.pop()
        insert_sorted_order(stack,element)
        stack.push(num)

if __name__ == '__main__':
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(10)
    print(stack.container)
    element = 5
    insert_sorted_order(stack,element)
    print(stack.container)