# reverse k'th first elements in a queue.

from collections import deque

class double_quque:
    def __init__(self,n):
        self.arr = deque()
        self.max_size = n
    
    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.max_size

    def push_front(self,data):
        if self.is_full():
            print("Queue is full")
            return 
        else:
            self.arr.appendleft(data)
    
    def pop_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.arr.popleft()

    def push_back(self,data):
        if self.is_full():
            print("Queue is full")
            return 
        else:
            self.arr.append(data)
    
    def pop_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.arr.pop()
    
    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            ans = self.arr.popleft()
            self.arr.appendleft(ans)
            return ans
    
    def get_rare(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            ans = self.arr.pop()
            self.arr.append(ans)
            return ans
    
    def q_size(self):
        return len(self.arr)


class Stack:
    def __init__(self,maxsize):
        self.container = deque()
        self.maxsize = maxsize
    
    def push(self,val):
        if self.is_full():
            print("Stack is full")
            return
        self.container.append(val)
        
    def pop(self):
        if self.is_empty():
           print("Stack is empty")
           return 
        self.container.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def is_full(self):
        return len(self.container)==self.maxsize

k = 3
dq = double_quque(5)
dq.push_back(1)
dq.push_back(2)
dq.push_back(3)
dq.push_back(4)
dq.push_back(5)

stack = Stack(k)

i = 0
while i < k:
    # Add k'th elements into stack.
    ele = dq.pop_front()
    stack.push(ele)
    i += 1

# print(dq.arr)

# Remove k'th elements from stack and push into Queue.
while not stack.is_empty():
    ele = stack.peek()
    stack.pop()
    dq.push_back(ele)


# remove N-K element from queue and push_back into queue.
t = dq.q_size() - k
while t:
    ele = dq.pop_front()
    dq.push_back(ele)
    t -= 1
print(dq.arr)    


