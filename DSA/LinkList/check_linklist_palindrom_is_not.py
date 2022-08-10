# linklist is palindrom or not.

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
   

    def is_palindrome_using_array(self):
        '''Return True if palindrome else False'''

        # Time complexity --> O(n) 
        # Space complexity --> O(n)

        
        array = []
        temp = self.start
        while temp != None:
            array.append(temp.data)
            temp = temp.next
        # 👀👇👀👇👀👇👀👇    sortcut.
        # print(array == array[::-1])
        start = 0 
        end = len(array)-1
        while start < end:
            if array[start] != array[end]:
                return False
            start += 1
            end -= 1
        return True


    def get_middle(self):
        slow = self.start
        fast = slow.next

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def revers_remening(self,temp):
        curr = temp
        prev = None

        while curr:
            forword = curr.next
            curr.next=prev
            prev = curr
            curr = forword
        return prev



    def is_palindrom_using_linkist_itself(self):
        # time complexity --> O(n).
        # space complexity --> O(1).
        if self.start == None or self.start.next == None:
            return True
        else:
            middle = self.get_middle()
            temp = middle.next
            middle.next = self.revers_remening(temp)
            head1 = self.start
            head2 = middle.next

            while head2:
                if head1.data != head2.data:
                    return False
                head1 = head1.next
                head2 = head2.next
            return True

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
# my_list.inser_at_last(1)
# my_list.inser_at_last(1)
# my_list.inser_at_last(1)
# my_list.inser_at_last(0)
# my_list.inser_at_last(1)
# my_list.inser_at_last(1)
# my_list.inser_at_last(1)

my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(2)
my_list.inser_at_last(1)


# my_list.view_data()


# val = my_list.is_palindrome_using_array()
val = my_list.is_palindrom_using_linkist_itself()

if val:
    print("Linklist is palindrome.")
else:
    print("Linklist is not palindrome.")









