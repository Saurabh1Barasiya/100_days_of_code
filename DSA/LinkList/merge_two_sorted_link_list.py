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
    
    def solve(self,first,second):
        if first.next == None:
            first.next = second
            return first
        else:
            prev = first
            curr = prev.next
            upload = second

            while upload != None and curr != None:
                if upload.data >= prev.data and upload.data <= curr.data:
                    prev.next = upload
                    forword = upload.next   # adress na ghume.
                    upload.next = curr

                    # update pointer
                    prev = upload
                    upload = forword
                else:
                    prev = curr
                    curr = curr.next

                    if curr == None:
                        prev.next = upload
                        return first  
            return first  

    def merge(self,first,secound):
        if first == None:
            return secound
        if secound == None:
            return first

        if first.data < secound.data:
            return self.solve(first,secound)
        else:
            return self.solve(secound,first)
        
        




         

        

my_list = Linklist()
my_list.inser_at_last(1)
my_list.inser_at_last(3)
my_list.inser_at_last(5)

my_list1 = Linklist()
my_list1.inser_at_last(2)
my_list1.inser_at_last(4)
my_list1.inser_at_last(5)


# my_list.view_data()
print()
# my_list1.view_data()

l3 = Linklist()
my_list.start = l3.merge(my_list.start,my_list1.start)
my_list.view_data()








