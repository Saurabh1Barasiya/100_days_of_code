#  reverse the queue.


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


# from collections import deque
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




qu = double_quque(6)
qu.push_back(4)
qu.push_back(3)
qu.push_back(1)
qu.push_back(10)
qu.push_back(2)
qu.push_back(6)

# print(qu.arr.reverse())  # by default method provided by deque class.
print(qu.arr)

# Initilized a stack.
stack = Stack(len(qu.arr))
while not qu.is_empty():
    popped = qu.pop_front()
    stack.push(popped)

while not stack.is_empty():
    top_element = stack.peek()
    stack.pop()
    qu.push_back(top_element)

print("resersed the queue", qu.arr)



# Time complexcity O(N).
# Space complexity is O(N).