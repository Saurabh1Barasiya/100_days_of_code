# will make tree using level order.

'''
1
3 5 
7 11 17
'''

from queue import Queue
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def build_leval_order_tree(root):
    q = Queue(sys.maxsize)
    data = int(input("Enter data for Root : "))
    root = Node(data)
    q.put(root)

    while not q.empty():
        temp = q.get()
        print(temp is root)
        input()
        left_data = int(input(f"Enter left data for {temp.data} : "))
        if left_data != -1:
            temp.left = Node(left_data)
            q.put(temp.left)
        
        right_data = int(input(f"Enter right data for {temp.data} : "))
        if right_data != -1:
            temp.right = Node(right_data)
            q.put(temp.right)
    return root


def leval_order_traversal(root):
    q = Queue(100)
    q.put(root)
    q.put(None)
    while not  q.empty():
        temp = q.get()
        if temp == None:
            print()
            if not q.empty():
                q.put(None)
        else:
            print(temp.data,end=" ")
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)


if __name__ == '__main__':
    root = None
    root = build_leval_order_tree(root)
    leval_order_traversal(root)