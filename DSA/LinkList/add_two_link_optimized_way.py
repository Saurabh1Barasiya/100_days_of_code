# add two link list in a very optimized way.

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
        final = Node(-1)  # dummy node.
        tail = final
        carry = 0
        
        while first != None or secound != None or carry != 0:
                # jab teeno condition false hogi tabhi loop se bahar niklege.

                val1 = 0  
                val2 = 0
                
                if first != None:
                    val1 = first.data
                
                if secound != None:
                    val2 = secound.data

                sum_ = carry + val1 + val2

                digit = sum_ % 10   
                tail.next = Node(digit)
                tail = tail.next

                carry = sum_ // 10

                # if first list end ho gayi h to first ko aage nahi jaba h.
                if first != None:
                    first = first.next

                # if secound list end ho gayi h to secound ko aage nahi jaba h.
                if secound != None:
                    secound = secound.next
        
        # 1 node aage jana padega kyoki first node me -1 data rakhha h
        final = final.next


        ans = self.reverse(final)
        return ans
        

    def add_two_lists_optimized_way(self,first,secound):


        first = self.reverse(first)
        secound = self.reverse(secound)
        
        ans = self.lets_add(first,secound)

        self.start = ans

        


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

my_call.add_two_lists_optimized_way(my_list.start,my_list1.start)
my_call.view_data()


