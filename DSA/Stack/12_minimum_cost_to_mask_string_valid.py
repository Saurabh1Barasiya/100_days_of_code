# minimum cost to string valid.
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

def min_cost_to_string_valid(stack,string):
    if len(string) % 2 == 1:
        return -1
    else:
        for i in string:
        # if opening so push .
            if i == "{":
                stack.push(i)
                # print("push hua h")
            else:
                # if closing milega.
                if not stack.is_empty() and  stack.peek() == "{":
                    # agar stack ke peek me { milegea or i me  } h to pop kar do.
                    # matlab valid bracket ko remove kar diya.
                    stack.pop()
                else:
                    # vadid ko remove karte karte satck empty ho gaya to.
                    stack.push(i)
                    # print("yaha push hoga : ", i)
        # ab hamare pass valid bracket nahi h.
        # {{{{
        # }}}}}
        # is type ke bracket bache h.
        a = b = 0
        while not stack.is_empty():
            if not stack.is_empty() and stack.peek() == "{":
                a+=1
            else:
                b+=1
            stack.pop()
        # print("value of b " , b)
        ans = ((a+1)//2) + ((b+1)//2)
        return ans


if __name__ == '__main__':
    string = "{{{{"
    stack = Stack(len(string))
    ans = min_cost_to_string_valid(stack,string)
    print(ans)
