class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.start = None
        # self.end = None
    
    

    def insert_at_last(self,data):
        if self.start == None:
            new_node = Node(data)
            self.start = new_node
        else:
            new_node = Node(data)
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    
    def reverse(self):
        curr = self.start
        back = None
        while curr != None :
            forword = curr.next
            curr.next = back
            curr.prev = forword
            back = curr
            curr = forword
        self.start = back

    def view_list(self):
        if self.start == None:
            print("Link list is empty.")
            return
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
            print()

if __name__ == '__main__':
    DL = DoubleLinkList()
    DL.insert_at_last(10)
    DL.insert_at_last(20)
    DL.insert_at_last(30)
    DL.insert_at_last(40)
    DL.reverse()
    
    DL.view_list()