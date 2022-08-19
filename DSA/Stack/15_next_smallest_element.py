#   [4,8,5,2,25]   --- >  [2, 5, 2, -1, -1]
#   [13,7,6,12]    --- >  [7, 6, -1, -1]
#   [13,13,21,3]   --- >  [3, 3, 3, -1]


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

def next_smaller_element(array,stack):
    stack.push(-1)
    i = len(array)-1
    while i >= 0:
        curr = array[i]
        while stack.peek() >= curr: 
            stack.pop()
        array[i] = stack.peek()
        stack.push(curr)
        i-=1

if __name__ == '__main__':
    # array = [4,8,5,2,25]
    # array = [13,7,6,12]
    array = [13,13,21,3]
    stack = Stack(len(array))
    next_smaller_element(array,stack)
    print(array)
