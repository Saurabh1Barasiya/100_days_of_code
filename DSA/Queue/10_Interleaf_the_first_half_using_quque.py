# 10_Interleaf_the_first_half_using_quque.py

# I/P --> [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# O/P --> [10, 60, 20, 70, 30, 80, 40, 90, 50, 100]


# Time complexcity worst case O(n).
# Space  complexity is O(n).


# but is question me hako stack ka use karke karna tha . hamne queue ka use kiya h.



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


def interleaf_first_half(old_quque, n):
    mid = n//2

    # create a new quque
    new_quque = double_quque(mid)
    for i in range(mid):
        popped_value = old_quque.pop_front()
        new_quque.push_back(popped_value)

    # print(new_quque.arr)


    # ab new queue ke front se element nikalo and old_queue me push_back kar do.
    # and old_queue ke front se element nikalo and old_queue me push_back kar do.

    while not new_quque.is_empty():
        new_quque_pop_value = new_quque.pop_front()
        old_quque.push_back(new_quque_pop_value)
        
        old_quque_pop_value = old_quque.pop_front()
        old_quque.push_back(old_quque_pop_value)
    
    return old_quque

if __name__ == '__main__':
    qu = double_quque(10)
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



