from collections import deque
from inspect import stack
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
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def is_full(self):
        return len(self.container)==self.maxsize


def knows(MATRIX,a,b):
    # return MATRIX[a][b]
    if MATRIX[a][b] == 1:
        return True
    else:
        return False


def findCelebrity(MATRIX,stack,n):
    # push all index to stack.
    for i in range(n):
        stack.push(i)

    # pop two index from stack and compare.
    while stack.size() > 1:
        a = stack.peek()
        stack.pop()
        b = stack.peek()
        stack.pop()

        if knows(MATRIX,a,b):
            stack.push(b)
        else:
            stack.push(a)
    
    ans = stack.peek()  # last element in stack.

    # check row.
    row_count = 0
    row_check = False

    for i in range(n):
        if MATRIX[ans][i] == 0:
            row_count += 1

    if row_count == n:
        row_check = True
    
    # cehck column.
    col_count = 0
    col_check = False
    
    for i in range(n):
        if MATRIX[i][ans] == 1:
            col_count += 1  

    if col_count == n-1:
        # because digonal ko remove karna tha.
        col_check = True

    if row_check and col_check:
        return ans
    else:
        return -1

if __name__ == "__main__":
    # M = [
    #     [0,1,0],
    #     [0,0,0],
    #     [0,1,0],
    #     ]

    MATRIX = [ 
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 1, 0 ] 
            ]
    # print(len(MATRIX))

    n = 3
    stack = Stack(n)
    id_ = findCelebrity(MATRIX,stack,n)
    print(id_)