class Circular_queue:
    def __init__(self,n):
        self.arr = [None] * n
        self.max_size = n
        self.front = -1
        self.rare = -1
    
    def push(self,data):
        # check queue is full .
        # if self.front == 0 and self.rare == self.max_size-1 or self.rare == self.front-1 % self.max_size-1:
        if(((self.rare+1) % self.max_size) == self.front):
            print("rare",self.rare)
            print("front",self.front)
            print("Queue is full ")
            return
        elif self.front == -1:
            self.front = self.rare = 0
            self.arr[self.rare] = data
        elif self.rare == self.max_size - 1 and self.front != 0:
            self.rare = 0
            self.arr[self.rare] = data
        else:
            self.rare += 1
            self.arr[self.rare] = data
    
    def pop(self):
        # cheack queue is empty.
        if self.front == -1:
            print("Empty queue")
            return
        else:
            ans = self.arr[self.front]
            self.arr[self.front] = -1

            if self.front == self.rare:
                self.rare = -1
                self.front = -1

            elif self.front  == self.max_size-1:
                self.front = 0
            else:
                self.front += 1
            return ans


cq = Circular_queue(5)
# print(cq.arr)
cq.push(10)
cq.push(20)
cq.push(30)
cq.push(40)
cq.push(50)
cq.pop()
cq.pop()
cq.push(70)
cq.push(80)
cq.push(90)
print(cq.arr)