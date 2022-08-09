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

    def delete_loop_link(self):
        starting_loop = self.is_floyd_cycle()
        if starting_loop == None:
            return
        
        temp = starting_loop
        while temp.next != starting_loop:
            temp = temp.next
        temp.next = None
        print("deleted loop")
        
    
    def view_list(self):
        temp = self.start
        while temp.next != self.start:
            print(temp.data , end = " ")
            temp = temp.next
        print(temp.data, end = " ")

    def show(self):
        temp = self.start
        while temp:
            print(temp.data, end = " ")
            temp = temp.next



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

cc.view_list()



# ans = cc.get_loop_node()
# if ans == None:
#     print("No loop")
# else:
#     print("\n Floyd Cycle or not : ",ans.data)
cc.delete_loop_link()
cc.show()
