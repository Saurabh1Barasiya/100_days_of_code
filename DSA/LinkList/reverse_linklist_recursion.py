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
    
    def view_data(self):
        if self.start == None:
            print("Link list is empty.") 
            return  
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
        
    def rev_recusion(self,curr,prev):
        if curr == None:
            self.start = prev
            return
        else:
            forword = curr.next
            self.rev_recusion(forword,curr)
            curr.next = prev

    def reverse_list(self):
        prev = None
        curr = self.start
        self.rev_recusion(curr,prev)


my_list = Linklist()

my_list.inser_at_last(100)
my_list.inser_at_last(200)
my_list.inser_at_last(300)
my_list.inser_at_last(400)
my_list.inser_at_last(500)
my_list.inser_at_last(600)
my_list.reverse_list()
my_list.view_data()