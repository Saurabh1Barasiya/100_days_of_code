# find previous smaller element.

#  [5,7,4,9,8,10]          --- >    [-1, 5, -1, 4, 4, 8]
#  [2, 5, 3, 7, 8, 1, 9]  ---- >    [-1, 2, 2, 3, 7, -1, 1]

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

def previous_smaller_element(stack,arr):
    # initially stack me -1 rahega.
    stack.push(-1)
    i = 0
    while i < len(arr):
        curr = arr[i]
        while stack.peek() >= curr:
            stack.pop()
        arr[i] = stack.peek()
        stack.push(curr)
        i+=1

if __name__ == "__main__":
    # array = [5,7,4,9,8,10]
    array = [2,5,3,7,8,1,9]
    stack = Stack(len(array))
    previous_smaller_element(stack,array)
    print(array)

    # [-1, 2, 2, 3, 7, -1, 1]

    # [-1, 5, -1, 4, 4, 8]