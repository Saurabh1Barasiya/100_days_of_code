# delete middle element on stack.

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

def delete_middle_element(stack,size,count):
    ''' this function will delete middle element in the stack. '''
    
    # base case. 
    if count == size // 2:
        stack.pop()
        return 
    else:
        num = stack.peek()
        stack.pop()

        # recursive case. 
        count += 1
        delete_middle_element(stack,size,count)
        stack.push(num)


def delete(stack,size):
    ''' this function will delete middle element in the stack. '''

    count = 0
    delete_middle_element(stack,size,count)
        


if __name__ == '__main__':
    size = 5
    stack = Stack(size)
    # stack.push(4)
    stack.push(6)
    stack.push(5)
    stack.push(7)
    stack.push(8)
    # print(stack.container)
    delete(stack,size)
    print(stack.container)