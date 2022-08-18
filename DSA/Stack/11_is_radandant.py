# check string is radandant or not.

# ----> ((a+b)) --> redandant .
# ----> (a+b) -->  not redandant .



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

def is_radandant(stack,string):
    # if opening h to push kero.
    for ch in string:
        if ch == '(' or ch == '+' or ch == '-' or ch == '*' or ch == '/':
            stack.push(ch)
        else:
            if ch == ')':
                # if closing h to top ko check kero and pop kero.
                radandant = True
                while stack.peek() != '(':
                    top = stack.peek()
                    if top == '+' or top == '-' or top == '*' or top == '/':   
                        radandant = False
                    stack.pop()
                if radandant == True:
                    return True
                stack.pop()
    return False                 


if __name__ == '__main__':
    string = "(a+b)"
    stack = Stack(len(string))
    ans = is_radandant(stack,string)
    print(ans)