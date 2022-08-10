# add two link list.

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

    def reverse(self,head):    
        curr = head
        prev = None
        while curr:
            forword = curr.next
            curr.next= prev
            prev = curr
            curr = forword
        return prev

    def lets_add(self,first,secound):
        final = Node(-1)
        tail = final
        # l1 = []
        carry = 0
        sum_ = 0

        while first != None and secound != None:
           sum_ = first.data + secound.data + carry
           digit = sum_ % 10 
        #    l1.append(digit) 
           tail.next = Node(digit)   
           tail = tail.next
           carry = sum_ // 10
           first = first.next
           secound = secound.next

        while first != None:
            sum_ = first.data + carry
            digit = sum_ % 10
            # l1.append(digit)
            tail.next = Node(digit)   
            tail = tail.next
            carry = sum_ // 10
            first = first.next 

        while secound != None:
            sum_ = secound.data + carry
            digit = sum_ % 10
            # l1.append(digit)
            tail.next = Node(digit)   
            tail = tail.next
            carry = sum_ // 10
            secound = secound.next  

        while carry != 0:
            digit = carry % 10
            # l1.append(digit)
            tail.next = Node(digit)   
            tail = tail.next
            carry = carry // 10

        final = final.next

        # print(l1)
        final = self.reverse(final)

        return final

        

    def add_two_lists(self,first,secound):


        first = self.reverse(first)
        secound = self.reverse(secound)
        
        ans = self.lets_add(first,secound)

        self.start = ans

        '''
        while first:
            print(first.data, end=" ")
            first = first.next
        print("")
        
        while secound:
            print(secound.data, end=" ")
            secound = secound.next
        '''


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
my_list.inser_at_last(9)
my_list.inser_at_last(8)
my_list.inser_at_last(7)

my_list1 = Linklist()
my_list1.inser_at_last(9)
my_list1.inser_at_last(6)
my_list1.inser_at_last(5)
my_list1.inser_at_last(4)
my_list1.inser_at_last(2)

print("first list : ",my_list.view_data())
print("secound list : ",my_list1.view_data())

my_call = Linklist()

my_call.add_two_lists(my_list.start,my_list1.start)
my_call.view_data()


