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



def valid_parinthesis(stack,exp):
    ''' this function will check valid parinthesis. '''
    # if bracket are opening parentheses so push it.'[' '{' '('.
    for i in exp:
        if i  in ['(','{','[']:
            stack.push(i)
    
        # if bracket are closing parentheses so pop it. ']','}',')'
        else:
            ch = i 
            if not stack.is_empty():
                if ( ch==")" and stack.peek()=="(" ) or ( ch=="}" and stack.peek()=="{" ) or ( ch=="]" and stack.peek()=="[" ):
                    stack.pop()
                else:
                    return False
            else:
                # stack empty h and closing bracket aa gaya. not good.
                return False
    
    if stack.is_empty():
        return True
    else:
        return False

 
# TC = O(n)  # 
# SC = O(n)  #





if __name__ == '__main__':
    # exp = '''[()]{}{[()()]()}'''
    exp = '''[(){}((()))]''' 

    ans = stack = Stack(len(exp))
    ans = valid_parinthesis(stack,exp)
    if ans:
        print("Balanced")
    else:
        print("Not Balanced ")
    