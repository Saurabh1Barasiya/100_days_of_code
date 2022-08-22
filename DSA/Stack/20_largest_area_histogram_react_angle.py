from collections import deque
class Stack:
    def __init__(self,maxsize):
        self.container = deque()
        self.maxsize = maxsize
    def is_empty(self):
        return len(self.container) == 0
    def is_full(self):
        return len(self.container) == self.maxsize
    def push(self,item):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.container.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.container.pop()
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.container[-1]

   
def previous_smaller_index(array):
    stack = Stack(len(array))
    prev_small_index = []
    i = 0
    while i < len(array):
        curr = array[i]
        while not stack.is_empty() and array[stack.peek()] >= curr:
            stack.pop()
        if stack.is_empty():
            prev_small_index.append(-1)
        else:
            prev_small_index.append(stack.peek())
        stack.push(i)
        i += 1
    print("previous index : ",prev_small_index)
    return prev_small_index


def next_smaller_index(array):
    stack = Stack(len(array))
    next_smaller_index = []
    i = len(array)-1
    while i >= 0:
        curr = array[i]
        while not stack.is_empty() and array[stack.peek()] >= curr:
            stack.pop()
        if stack.is_empty():
            next_smaller_index.append(len(array))
        else:
            next_smaller_index.append(stack.peek())
        stack.push(i)
        i-=1
    next_smaller_index.reverse()
    print("next index : ",next_smaller_index)
    return next_smaller_index



def max_area_histogram(array):
    ns = next_smaller_index(array)
    ps = previous_smaller_index(array)

    i = 0
    max_area = 0
    while i < len(array):
        area = (ns[i]-ps[i]-1)*array[i]
        max_area = max(max_area,area)
        i += 1
    return max_area

if __name__ == '__main__':
    hist = [6, 2, 5, 4, 5, 1, 6]
    print("Maximum area is",
    max_area_histogram(hist))