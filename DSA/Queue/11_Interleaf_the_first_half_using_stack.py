

# i/p --->  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# o/p --->  [10, 60, 20, 70, 30, 80, 40, 90, 50, 100]

# Note.
# The given queue will always be of even length.


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


def interleaf_first_half(queue, n):
    mid = n // 2
    stack = Stack(mid)

    # push first half of queue into stack.
    for i in range(mid):
        stack.push(queue.pop_front())

    # get_item from stack and push_back into queue.
    while not stack.is_empty():
        value = stack.peek()
        stack.pop()
        queue.push_back(value)
    
    # first half of queue ko peeche laga do.
    for i in range(mid):
        popped_value = queue.pop_front()
        queue.push_back(popped_value)
    
    # first half of queue ko fir se stack me dalo.
    for i in range(mid):
        stack.push(queue.pop_front())
    

    # ab stack se pop kero and queue me push_back kero and,
    # queue ke front se push kero and queue me push_back kero jab tak stack empty na ho jay.

    while not stack.is_empty():
        val = stack.peek()
        stack.pop()
        queue.push_back(val)
        val2 = queue.pop_front()
        queue.push_back(val2)
    
    return queue
    

if __name__ == '__main__':
    qu = double_quque(10)
    # qu.push_back(11)
    # qu.push_back(12)
    # qu.push_back(13)
    # qu.push_back(14)
    # qu.push_back(15)
    # qu.push_back(16)
    # qu.push_back(17)
    # qu.push_back(18)
    
    qu.push_back(10)
    qu.push_back(20)
    qu.push_back(30)
    qu.push_back(40)
    qu.push_back(50)
    qu.push_back(60)
    qu.push_back(70)
    qu.push_back(80)
    qu.push_back(90)
    qu.push_back(100)
    
    n = qu.q_size()
    ans = interleaf_first_half(qu, n)
    print(ans.arr)
