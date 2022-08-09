# sort 0s 1s and 2s in a link list.
import copy

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


    def insert_at_tail(self,tail,curr):
        print("---------------->",curr.data)
        tail.next = curr
        tail = tail.next

    def sort(self):
        # yaha par ham data ko change kar dege.
        curr = self.start
        zero_head = Node(-1)
        zero_tail = zero_head
        one_head = Node(-1)
        one_tail = one_head
        two_head = Node(-1)
        two_tail = two_head

        while curr != None:
            value = curr.data
            if value == 0:
                # print(" value ------------>")
                self.insert_at_tail(zero_tail,curr)
            elif value == 1:
                # print(" value 1 ------------------->")
                self.insert_at_tail(one_tail,curr)
            elif value == 2:
                # print(" value 2 ------------------->")
                self.insert_at_tail(two_tail,curr)
            curr = curr.next

        zero_tail=zero_tail.next
        while zero_tail:
            print(zero_tail.data, end="")
            zero_tail=zero_tail.next
        print("")


        one_tail=one_tail.next
        while one_tail:
            print(one_tail.data, end="")
            one_tail=one_tail.next
        print("")


        two_tail=two_tail.next
        while two_tail:
            print(two_tail.data, end="")
            two_tail=two_tail.next
        print("")

    def view_data(self):
        if self.start == None:
            print("Link list is empty.") 
            return  
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
        print("")
            
my_list = Linklist()

my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)

my_list.view_data()

my_list.sort()










