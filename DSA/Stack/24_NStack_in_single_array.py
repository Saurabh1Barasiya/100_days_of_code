# Nstack in a single array.

class Nstack:
    def __init__(self,sn,element):
        self.arr = [0]*element
        self.top = [-1]*sn
        self.next = [i+1 for i in range(element)]
        self.next[-1] = -1
        self.free_spot = 0

        print("arr",self.arr)
        print("next",self.next)
        print("top",self.top)
    
    def push(self,data,m):
        # first we check stack is full or not .
        if self.free_spot == -1:
            return "Stack is full"
            
        else:
            index = self.free_spot

            # update free_spot
            self.free_spot = self.next[index]

            # add data in array.
            self.arr[index] = data
            
            self.next[index] = self.top[m-1]

            self.top[m-1] = index

    def pop(self,m):
        # check stack is empty.
        if self.top[m-1] == -1:
            return "Stack is empty"
            
        else:
            # simple push ka reverse kar do.
            index = self.top[m-1]
            self.top[m-1] = self.next[index]
            self.next[index] = self.free_spot
            self.free_spot = index
            return self.arr[index]


ts = Nstack(3,6)
ts.push(10,1)
ts.push(20,1)
ts.push(30,2)
ts.push(40,2)
ts.push(50,3)
ts.push(60,3)
ts.push(70,3)

# print("after push")
# print("arr",ts.arr)
# print("next",ts.next)
# print("top",ts.top)


# print(ts.pop(3))
# print(ts.pop(3))
# print(ts.pop(2))
# print(ts.pop(2))
# print(ts.pop(1))
# print(ts.pop(1))


# print("after pop")
# print("arr",ts.arr)
# print("next",ts.next)
# print("top",ts.top)


# ts.push(100,1)
# print(ts.pop(1))


# ts.push(100,1)
# ts.push(200,1)
# ts.push(300,1)
# ts.push(400,1)
# ts.push(500,1)
# ts.push(600,1)

# print(ts.pop(1))
# print(ts.pop(1))
# print(ts.pop(1))
# print(ts.pop(1))
# print(ts.pop(1))
# print(ts.pop(1))