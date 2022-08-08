# remove duplicate form a unorderd linkkist.

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
    
    def remove_duplicates(self):
        '''
        #      O(n^2)---- > T.C
        #      O(1)  ---- > S.C
        curr = self.start
        while curr != None:
            prev = curr
            forword = curr.next
            while forword != None:
                if forword.data == curr.data:
                    prev.next = forword.next
                    #forword = forword.next
                else:
                    prev = forword
                    #forword = forword.next
                forword = forword.next
            curr = curr.next
        '''

        
        # map or array ka concept.
        #      O(n) ---- > T.C
        #      O(n)  ---- > S.C
        curr = self.start  
        prev = None  
        visited = {}
        while curr != None:
            if curr.data  in visited:
                prev.next = curr.next
            else:
                visited[curr.data] = True
                prev = curr
            curr = curr.next

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



my_list.inser_at_last(100)
my_list.inser_at_last(100)
my_list.inser_at_last(100)
my_list.inser_at_last(300)
my_list.inser_at_last(400)
my_list.inser_at_last(200)

my_list.inser_at_last(300)
my_list.inser_at_last(300)
my_list.inser_at_last(500)
my_list.inser_at_last(200)

my_list.inser_at_last(400)
my_list.inser_at_last(500)


my_list.view_data()


my_list.remove_duplicates()
print("\n")
my_list.view_data()
