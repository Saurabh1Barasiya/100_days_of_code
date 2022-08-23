# Two stack in single array.
class two_stack:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = self.size
    
    def push1(self,data):
        # check atleast one space available in array.
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = data
        else:
            print("Stack Overflow full : ")
    
    def push2(self, data):
        # check atleast one space available in array.
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = data
        else:
            print("Stack Overflow full : ")
    
    def pop1(self):
        if self.top1 >= 0:
            top_value = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return top_value
        else:
            print("stack Underflow empty : ")
    
    def pop2(self): 
        if self.top2 < self.size:
            top_value = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return top_value
        else:
            print("stack Underflow empty : ")

ts = two_stack(5)
ts.push1(10)
ts.push1(20)
ts.push1(30)
ts.push1(40)
ts.push1(60)
ts.pop1()
ts.pop1()
ts.pop1()
ts.pop1()
ts.pop1()


ts.push2(50)
ts.push2(50)
ts.push2(50)
ts.push2(50)
ts.push2(50)
print(ts.pop2())
print(ts.pop2())
print(ts.pop2())
print(ts.pop2())
print(ts.pop2())
