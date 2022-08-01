class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.start = None

    def insert_At_beg(self,data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            return
        else:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node

    
    def inser_at_last(self,data):
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next= new_node

    def insert_at_pos(self,position,data):
        ini_len = self.get_length()
        new_node = Node(data)
        if position == 1:
            self.insert_At_beg(data)
            return
        elif position ==  ini_len:
            self.inser_at_last(data)
            return
        else:
            temp = self.start
            count = 1
            while count < position - 1:
                temp = temp.next
                count += 1
            
            new_node.next = temp.next
            temp.next = new_node

    def get_length(self):
        temp = self.start
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def delete_at_beg(self):
        if self.start == None:
            print("Link list is empty.")
            return
        else:
            self.start = self.start.next

    def delete_at_pos(self,position):
        if position == 1:
            self.delete_at_beg()
            return
        else:
            prev = None
            curr = self.start
            count = 1
            while count < position:
                prev = curr
                curr = curr.next
                count += 1

            prev.next = curr.next
            print(f"\n node {position} has been deleted")

    def view_data(self):
        if self.start == None:
            print("Link list is empty.") 
            return  
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
            # print("start pointer data.",self.start.data)


my_list = Linklist()
# my_list.insert_At_beg(10)
# my_list.insert_At_beg(20)
# my_list.insert_At_beg(30)
# my_list.insert_At_beg(40)
# my_list.insert_At_beg(50)


my_list.inser_at_last(100)
my_list.inser_at_last(200)
my_list.inser_at_last(300)
my_list.inser_at_last(400)
my_list.inser_at_last(500)
my_list.inser_at_last(600)
# my_list.insert_at_pos(1,500)
# my_list.insert_at_pos(1,600)
# my_list.insert_at_pos(6,700)
my_list.view_data()
# my_list.delete_at_beg()
# print("\nafter deletion")
# my_list.view_data()
# print(my_list.get_length())

my_list.delete_at_pos(4)
my_list.delete_at_pos(2)
my_list.delete_at_pos(1)
my_list.delete_at_pos(3)
my_list.view_data()