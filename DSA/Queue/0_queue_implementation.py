# queue implementation using Array.

# queue work as a first in first order.
# jo pahle aayega vahi pahle jayega.


class Queue:
    def __init__(self,n):
        self.arr = [None]*n
        self.maxsize = n
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.rear == self.maxsize
    
    def get_size(self):
        return self.size
    
    def push(self,data):
        # cheack queue is full.
        if self.is_full():
            print("Queue is full")
            return
        else:
            self.arr[self.rear] = data   
            self.rear += 1
            
            # just increment the size.
            self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            ans = self.arr[self.front]
            self.arr[self.front] = -1
            self.front += 1
            if self.front == self.rear:
                self.front = 0
                self.rear  = 0
            
            # just decrement the size.
            self.size = self.size - 1
            return ans
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        return self.arr[self.front]

queue = Queue(5)
# print(queue.is_empty())
# print(queue.is_full())

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.push(50)

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

# print(queue.peek())
print("size of queue : ",queue.get_size())