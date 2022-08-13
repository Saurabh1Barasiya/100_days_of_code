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

    def merge_two_list(self,first,secound):
        if first == None:
            return secound
        if secound == None:
            return first

        dummy = Node(0)
        tail = dummy
        
        while first != None and secound != None:
            if first.data < secound.data:
                new_node = Node(first.data)
                tail.next = new_node
                tail = new_node
                first = first.next
            else:
                new_node = Node(secound.data)
                tail.next = new_node
                tail = new_node
                secound = secound.next
        

        while first != None:
            new_node = Node(first.data)
            tail.next = new_node
            tail = new_node
            first = first.next

        while secound != None:
            new_node = Node(secound.data)
            tail.next = new_node
            tail = new_node
            secound = secound.next
        
        tail.next = None

        merged = dummy.next

        return merged
        # while temp != None:
        #     print(temp.data,end=" ")
        #     temp = temp.next
        
    def view_data(self):
        if self.start == None:
            print("Link list is empty.") 
            return  
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next


first = Linklist()


first.inser_at_last(1)
first.inser_at_last(5)
first.inser_at_last(7)
first.inser_at_last(9)
first.inser_at_last(11)


secound = Linklist()
secound.inser_at_last(2)
secound.inser_at_last(4)
secound.inser_at_last(6)
secound.inser_at_last(12)


# first.view_data()
# print()
# secound.view_data()


l3 = Linklist()
l3.start = l3.merge_two_list(first.start,secound.start)

l3.view_data()



