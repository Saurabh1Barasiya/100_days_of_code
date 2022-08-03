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
    

    def is_circular(self):
        if self.start == None:
            return True
        
        temp = self.start.next
        while temp != None and temp != self.start:
            temp = temp.next
        
        if temp == self.start:
            return True
        else:
            return False


    
    def view_list(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.data , end = " ")
            temp = temp.next
        print(temp.data, end = " ")




cc = Circular_list()
cc.insert_At_beg(4)
# cc.insert_At_beg(5)
# cc.insert_At_beg(6)
# cc.insert_At_beg(7)

# cc.insert_at_last(8)
# cc.insert_at_last(9)
# cc.insert_at_last(10)
# cc.insert_At_beg(1)
# cc.insert_at_last(20)
# cc.insert_at_last(30)
# cc.insert_at_data(1,100)
# cc.insert_at_data(8,100)
# cc.insert_at_data(30,100)

# cc.view_list()

ans = cc.is_circular()
print("\n Circular or not : ",ans)
