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
   

    def is_palindrome(self):
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
my_list.inser_at_last(1)
my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(1)
my_list.inser_at_last(1)
# my_list.inser_at_last(1)


my_list.view_data()


val = my_list.is_palindrome()
if val:
    print("Linklist is palindrome.")
else:
    print("Linklist is not palindrome.")









