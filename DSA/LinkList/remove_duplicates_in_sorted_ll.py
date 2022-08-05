# remove duplicate form a sorted linkkist.

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
    
    def remove_duplicates(self):
        curr = self.start
        while curr != None:
            if (curr.next != None) and (curr.data == curr.next.data):
                curr.next = curr.next.next
            else:
                curr = curr.next


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
my_list.inser_at_last(200)
my_list.inser_at_last(300)
my_list.inser_at_last(300)
my_list.inser_at_last(300)
my_list.inser_at_last(400)


my_list.view_data()


my_list.remove_duplicates()
print("\n")
my_list.view_data()