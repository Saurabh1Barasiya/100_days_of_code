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
    
    def get_length(self):
        count = 0
        temp = self.start
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def find_middle_node(self):
        ans = self.get_length()
        num = 0
        mid = ans//2
        temp = self.start
        while num < mid:
            temp = temp.next
            num += 1
        return temp.data
        

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

my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(3)
my_list.inser_at_last(4)

print(my_list.find_middle_node())
my_list.view_data()