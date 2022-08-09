#  0s 1s and 2s sorting in linklist using adress.

class Node:
    '''
    # 👀👀👀👀👀👀👀
    to create a new node
    '''
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    '''
    # 👀👀👀👀👀👀👀
    creating link list.
    '''
    def __init__(self):
        self.start = None
    

    def inser_at_last(self,data):
        '''
        # 👀👀👀👀👀👀👀
        insert newnode at last.
        '''
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next= new_node

    def create_link(self):
        '''
        # 👀👀👀👀👀👀👀
        create 0s 1s and 2s link list.
        '''

        # first we create Dummy nodes.
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        # 👀👀👀👀👀👀👀
        zero_tail = zero_head
        one_tail = one_head
        two_tail = two_head

        curr = self.start
        while curr != None:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
                curr = curr.next

            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
                curr = curr.next
            else:
                two_tail.next = curr
                two_tail = two_tail.next
                curr = curr.next

        # 👀👀👀👀👀👀👀
        # print zero link list.


        zero_tail.next = None
        one_tail.next = None
        two_tail.next = None

        '''
        zero_head=zero_head.next
        while zero_head :
            print(zero_head.data, end=" ")
            zero_head=zero_head.next

        
        # 👀👀👀👀👀👀👀
        # print one link list.
        one_head=one_head.next
        print("")
        while one_head:
            print(one_head.data, end=" ")
            one_head=one_head.next

        # 👀👀👀👀👀👀👀
        # print two link list.
        two_head=two_head.next
        print("")
        while two_head:
            print(two_head.data, end=" ")
            two_head=two_head.next
        '''
        
        '''
        # merging. 
        # 👀👀👀👀👀👀👀
        zero_tail.next = one_head.next
        one_tail.next = two_head.next
        two_tail.next = None
        self.start = zero_head.next
        '''
        
    
        # merging with no errors.
        if one_head.next != None:
            zero_tail.next = one_head.next
        else:
            zero_tail.next = two_head.next
        one_tail.next = two_head.next

        self.start = zero_head.next

    def view_data(self):
        '''
        👀👀👀👀👀👀👀
        print data of link list.
        '''
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
my_list.inser_at_last(0)
my_list.inser_at_last(2)
my_list.inser_at_last(2)
my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)



my_list.create_link()
# print("-----------------------------------------------")

my_list.view_data()