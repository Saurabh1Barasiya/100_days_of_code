# i/p  1:100 --> 2:200 --> 3:300 --> 4:400 --> 5:300

# o/p 3:

# if loop h to loop ka starting node hamko dedo.

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
    

    
    def is_floyd_cycle(self):
        if self.start == None:
            return None
        
        slow = self.start
        fast = self.start
        while slow != None and fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                return slow
        return None

    def get_loop_node(self):
        intersection = self.is_floyd_cycle()
        if intersection == None:
            return None
        temp = self.start
        while temp != intersection:
            temp = temp.next
            intersection = intersection.next
        return temp
    
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


ans = cc.get_loop_node()
if ans == None:
    print("No loop")
else:
    print("\n Floyd Cycle or not : ",ans.data)
