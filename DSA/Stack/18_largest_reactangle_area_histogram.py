from collections import deque
class Stack:
    def __init__(self,maxsize):
        self.container = deque()
        self.maxsize = maxsize
    
    def push(self,val):
        if self.is_full():
            raise Exception("Stack is full")
        self.container.append(val)
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.container.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def is_full(self):
        return len(self.container)==self.maxsize

def previous_smaller_index(array):
    stack = Stack(len(array))
    index_arr = []
    i = 0
    while i < len(array):
        curr = array[i]
        while not stack.is_empty() and array[stack.peek()] >= curr:
            stack.pop()
        if stack.is_empty():
            index_arr.append(-1)
        else:
            index_arr.append(stack.peek())
        stack.push(i)
        i+=1
    return index_arr

def next_smaller_index(array):
    stack = Stack(len(array))
    index_arr = []
    i = len(array) - 1
    while i >= 0:
        curr = array[i]
        while not stack.is_empty() and array[stack.peek()] >= curr:
            stack.pop()
        if stack.is_empty():
            index_arr.append(len(array))
        else:
            index_arr.append(stack.peek())
        stack.push(i)
        i-=1
    index_arr.reverse()
    return index_arr

def largest_area_react_Angle(array):
    max_area = 0
    ps = previous_smaller_index(array)
    ns = next_smaller_index(array)
    print("previous : ",ps)
    print("next : ",ns)
    i = 0
    while i < len(array):
        curr = (ns[i]-ps[i]-1)*array[i]
        max_area = max(max_area,curr)
        i+=1
    return max_area

if __name__ == '__main__':
    array = [6, 2, 5, 4, 5, 1, 6]
    # array = [3,1,2,4]
    ans = largest_area_react_Angle(array)
    print(ans)