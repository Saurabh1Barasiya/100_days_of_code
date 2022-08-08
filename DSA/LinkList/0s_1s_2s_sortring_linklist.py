# sort 0s 1s and 2s in a link list.

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


    def sort(self):
        # yaha par ham data ko change kar dege.
        zero_count = 0
        one_conunt = 0
        two_count = 0
        temp = self.start
        while temp != None:
            if temp.data == 0:
                zero_count += 1
            elif temp.data == 1:
                one_conunt += 1
            elif temp.data == 2:
                two_count += 1
            temp = temp.next
        
        temp = self.start
        while temp != None:
            if zero_count != 0:
                temp.data = 0
                zero_count -= 1
            elif one_conunt != 0:
                temp.data = 1
                one_conunt -= 1
            elif two_count != 0:
                temp.data = 2
                two_count -= 1
            temp = temp.next
        

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

my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)

my_list.view_data()

my_list.sort()
print("\n")
my_list.view_data()










