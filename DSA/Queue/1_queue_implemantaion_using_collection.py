# Queue implemantation using Array.

from collections import deque   
# a = deque([1,2,3])


# pop() last se pop karta h and popleft() first se pop karega.
# appaned() last me add karta h and appendleft first me add karega.


from collections import deque

class Queue:
    def __init__(self,n):
        self.arr = deque()
        self.maxsize = n
    
    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.maxsize
    
    def size(self):
        return len(self.arr)

    def push(self,data):
        if self.is_full():
            print("Queue is full ")
            return
        else:
            self.arr.appendleft(data)
    
    def pop(self):
        if self.is_empty():
            print("Queue is empty ")
            return
        ans = self.arr.pop()
        return ans



que = Queue(5)
que.push(10)
que.push(20)
que.push(30)
que.push(40)
que.push(50)

print(que.arr)

print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())