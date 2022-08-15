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


'''
def reverse_string(stack,string): 
    ans = ''
    
    # insert elements in stack.
    for i in string:
        stack.push(i)
    
    # pop and add to ans .
    for i in range(len(string)):
        ans += stack.pop()

    return ans
'''

def reverse_string(stack,string): 
    # push elements into a stack.
    ans = ""
    for item in string:
        stack.push(item)

    # while stack.is_empty() == False:
    #     element = stack.pop()
    #     ans += element

    while not stack.is_empty():
        element = stack.pop()
        ans += element
    
    return ans


if __name__ == '__main__':
    string = "saurabh"
    stack = Stack(len(string))
    ans = reverse_string(stack,string)
    print(ans)