# create saperate linklist of 0s 1s and 2s.


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


    def insert_at_tail(self,tail,curr):
        '''
        # 👀👀👀👀👀👀👀
        insert newnode at tail.
        '''

        # 👀👀👀👀👇👇👇👇👇
        # ye function sahi se kaam nahi kar raha h.
        # jo output muje chahiye vo nahi mil raha h.


        # print("---------------->",curr.data)

        tail.next = curr
        tail = tail.next

        # 👀👀👀👀👀👀👀
        # me haha par tail ke next me curr ko point kar rahe h. ok   ✔✔✔✔✔
        # but jab me tail ko update kar raha hu tab issue ho raha h. 🤦‍♀️🤦‍♀️🤦‍♀️

        # sir please help me so solve this problem 🙏🙏🙏🙏🙏🙏🙏.



        


    def create_link(self):
        '''
        # 👀👀👀👀👀👀👀
        create 0s 1s and 2s link list.
        '''

        

        curr = self.start

        zero_head = Node(-1)
        zero_tail = zero_head

        # initial me zerohead and zerotail same address ko point kar rahe h .
        # but jab ham new node insert karege to zerotail ko aage bada dege.

        one_head = Node(-1)
        one_tail = one_head

        # initial me onehead and onetail same address ko point kar rahe h .
        # but jab ham new node insert karege to onetail ko aage bada dege.

        two_head = Node(-1)
        two_tail = two_head

        
        # initial me twohead and twotail same address ko point kar rahe h .
        # but jab ham new node insert karege to twotail ko aage bada dege.


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

        # 👀👀👀👀👀👀👀
        # print zero link list.
        zero_tail=zero_tail.next
        while zero_tail:
            print(zero_tail.data, end="")
            zero_tail=zero_tail.next
        print("")


        # 👀👀👀👀👀👀👀
        # print one link list.
        one_tail=one_tail.next
        while one_tail:
            print(one_tail.data, end="")
            one_tail=one_tail.next
        print("")


        # 👀👀👀👀👀👀👀
        # print two link list.
        two_tail=two_tail.next
        while two_tail:
            print(two_tail.data, end="")
            two_tail=two_tail.next
        print("")


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
my_list.inser_at_last(2)
my_list.inser_at_last(0)
my_list.inser_at_last(1)
my_list.inser_at_last(2)

my_list.view_data()

my_list.create_link()










