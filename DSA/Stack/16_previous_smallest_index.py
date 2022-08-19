# find previous smaller index .

# [5,7,4,9,8,10] ----->  [-1, 0, -1, 2, 2, 4].

# [4,2,1,5,6,3,2,4,2] ----->   [-1, -1, -1, 2, 3, 2, 2, 6, 2].

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

def previous_smaller_index(stack,array):
    index_arr = []
    i = 0
    while i < len(array):
        curr = array[i]
        while not stack.is_empty() and array[stack.peek()] >= curr:
            stack.pop()
        if stack.is_empty():
            index_arr.append(-1)
        else:
            index_arr.append(stack.peek())
        stack.push(i)
        i+=1
    return index_arr


if __name__ == '__main__':
    # array = [5,7,4,9,8,10]
    # array = [4,2,1,5,6,3,2,4,2]
    array = [3,1,2,4]
    stack = Stack(len(array))
    ans = previous_smaller_index(stack,array)
    print(ans)
