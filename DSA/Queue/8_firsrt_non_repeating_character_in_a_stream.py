# first non repeating character in a stream.

# aabc ---> a#bb

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

def first_non_repeating(A):
    count = {}
    qu = double_quque(len(A))
    ans = ""
    # ininilize a dictionary.
    for ch in A:
        count[ch] = 0

    for ch in A:
        count[ch] += 1

        qu.push_back(ch)

        while not qu.is_empty():
            if count[qu.get_front()] > 1:
                qu.pop_front()
            else:
                ans += qu.get_front()
                break
        if qu.is_empty():
            ans += "#"
    return ans    

A = "aabc"
A = "zz"
ret_val = first_non_repeating(A)
print(ret_val)
