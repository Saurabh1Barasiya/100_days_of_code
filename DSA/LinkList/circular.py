class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_list:
    def __init__(self):
        self.start = None

    def insert_At_beg(self,data):
        if self.start == None:
            new_node = Node(data)
            self.start = new_node
            self.start.next = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            # insert at beginning .    
            new_node = Node(data)
            temp.next = new_node
            new_node.next = self.start
            self.start = new_node
    
    def insert_at_last(self, data):
        # suppose we have already list.
        temp = self.start
        while temp.next != self.start:
            temp = temp.next

        new_node = Node(data)

        # 👀👀👀👀👀👀 ye bhi sahi h.
        # new_node.next = self.start
        # temp.next = new_node

        new_node.next = temp.next
        temp.next = new_node

    def insert_at_data(self, locdata, data):
        # assume kar rahe h ki data pesent h linklist me.
        if self.start.data == locdata:
            self.insert_At_beg(data)
            return
        else:
            back = None
            curr = self.start
            while curr.data != locdata:
                back = curr
                curr = curr.next

            new_node = Node(data)
            new_node.next = back.next
            back.next = new_node

    def delete_beg(self):
        if self.start == None:
            print("linklist is empty")
            return
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            '''
            👀👀👀👀👀👀👀👀👀  both condition are work well .
            # self.start = self.start.next
            # temp.next = self.start
            '''
            temp.next = self.start.next
            self.start = self.start.next

    def delete_at_last(self):
        if self.start == None:
            print("linklist is empty")
            return
        else:
            back = None
            curr = self.start
            while curr.next != self.start:
                back = curr
                curr = curr.next
            back.next = curr.next
            del curr

    def view_list(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.data , end = " ")
            temp = temp.next
        print(temp.data, end = " ")




cc = Circular_list()
cc.insert_At_beg(4)
cc.insert_At_beg(5)
cc.insert_At_beg(6)
cc.insert_At_beg(7)

cc.insert_at_last(8)
cc.insert_at_last(9)
cc.insert_at_last(10)
cc.insert_At_beg(1)
cc.insert_at_last(20)
cc.insert_at_last(30)
cc.insert_at_data(1,100)
cc.insert_at_data(8,100)
cc.insert_at_data(30,100)
cc.delete_beg()
cc.delete_beg()
cc.delete_beg()
cc.delete_at_last()
cc.delete_at_last()
cc.delete_at_last()
cc.delete_at_last()
cc.view_list()
