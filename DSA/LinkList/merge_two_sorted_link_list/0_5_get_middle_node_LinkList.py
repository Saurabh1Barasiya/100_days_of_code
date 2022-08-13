class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.start = None

    
    def inser_at_last(self,data):
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next= new_node

    def get_moddle_node(self):
        if self.start == None:
            print("Link list is empty.") 
            return
        else:
            slow = self.start
            fast = slow.next
            while fast != None and fast.next != None:
                fast=fast.next
                fast=fast.next
                slow=slow.next
            print("Slow ka data : ",slow.data)

    def view_data(self):
        if self.start == None:
            print("Link list is empty.") 
            return  
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next


my_list = Linklist()


my_list.inser_at_last(100)
my_list.inser_at_last(200)
my_list.inser_at_last(300)
my_list.inser_at_last(400)
my_list.inser_at_last(500)
my_list.inser_at_last(600)


my_list.view_data()
print()
my_list.get_moddle_node()