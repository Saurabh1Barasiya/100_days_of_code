from hashlib import new
from shutil import which


class Node:
    '''for creating a single node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    '''for making a linklist'''
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        '''insert a node at the beginning of the linklist'''
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        '''print the linklist'''
        temp = self.head
        if temp is None:
            print("Linklist is empty")
        else:
            while temp:
                print(f"{temp.data} --->", end = ' ')
                temp = temp.next

    def insert_at_end(self,data):
        '''insert a node at the end of the linklist'''
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node

    def insert_at_pos(self,data,pos):
        if self.head is None:
            print("Linklist is empty") 
        else:
            temp = self.head
            while temp.next is not None:
                if temp.data == pos:
                    break
                temp = temp.next
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
    
    def insert_before(self,data,x):
        if self.head is None:
            print("Linklist is empty")
        else:
            if self.head.data == x:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    if temp.next.data == x:
                        break
                    temp = temp.next
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node

obj = Linklist()
obj.insert_at_beg(1)
obj.insert_at_beg(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.insert_at_end(5)
obj.insert_at_end(6)
obj.insert_at_end(7)
obj.insert_at_end(8)
obj.insert_at_end(9)
obj.insert_at_pos(20,6)
obj.insert_before(50,1)
obj.insert_before(100,6)
obj.insert_before(72,7)

obj.print_list()