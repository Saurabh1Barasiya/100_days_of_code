# i double ended queue .


# ye compleate nahi h isme kush issue h.

class Double_queue:
    def __init__(self,n):
        self.arr = [None]*n
        self.max_size = n 
        self.front = -1
        self.rare = -1

    def rare_push_start(self,data):
        if ((self.rare + 1) % (self.max_size)) == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            # first element.
            self.front = self.rare = 0
        elif (self.rare == (self.max_size -1 )) and self.front != 0:
            self.rare = 0
        else:
            self.rare += 1
        self.arr[self.rare] = data
    
    def front_pop_start(self):
        if self.front == -1:
            print("Queue is empty")
            return
        else:
            ans = self.arr[self.front]
            self.arr[self.front] = -1

            if self.front == self.rare:
                # single element.
                self.front = self.rare = -1
            elif self.front == self.max_size - 1:
                self.front = 0
            else:
                self.front += 1

    def rare_push_back(self,data):
        if ((self.rare - 1) % (self.max_size)) == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            # first element.
            self.front = self.rare = 0
        elif (self.rare == 0) and (self.front != self.max_size-1):
            self.rare = self.max_size - 1
        else:
            self.rare -= 1
        self.arr[self.rare] = data

dq = Double_queue(5)
dq.rare_push_back(10)
dq.rare_push_back(20)
dq.rare_push_back(30)
dq.rare_push_back(40)
dq.rare_push_back(50)
print(dq.arr)

