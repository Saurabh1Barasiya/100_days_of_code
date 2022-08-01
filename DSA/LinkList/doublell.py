class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.start = None
        # self.end = None
    
    def insert_at_beg(self,data):
        if self.start == None:
            new_node = Node(data)
            self.start = new_node
        else:
            new_node = Node(data)
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        temp = self.start
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # 👀👀👀 two pointer.
    # def insert_at_pos(self, position,data):
    #     if position == 1:
    #         self.insert_at_beg(data)
    #         return
    #     else:
    #         count = 1       
    #         curr = self.start
    #         back = None
    #         while count < position:
    #             back = curr
    #             curr = curr.next
    #             count += 1
            
    #         # insert at last position
    #         if curr.next == None:
    #             self.insert_at_last(data)
    #             return
    #         else:
    #             new_node = Node(data)
    #             back.next = new_node
    #             new_node.next = curr
    #             new_node.prev = back
    #             curr.prev = new_node

    # single pointer
    def insert_at_pos(self, position,data):
        if position == 1:
            self.insert_at_beg(data)
            return
        else:
            count = 1       
            temp = self.start
            while count < position-1:
                temp = temp.next
                count += 1
            
            # insert at last position
            if temp.next == None:
                self.insert_at_last(data)
                return
            else:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next.prev = new_node
                new_node.prev = temp
                temp.next = new_node
                


    def delete_at_pos(self,position):
        # hame yaha temp ko bhi lena padega.
        if position == 1:
            temp = self.start 
            temp.next.prev = None
            self.start = temp.next
            temp.next = None
            # del temp
        else:
            back = None
            curr = self.start  
            count = 1
            while count < position: 
                back = curr
                curr = curr.next
                count += 1
            curr.prev = None
            back.next = curr.next
            curr.next = None
            del curr

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
    DL.insert_at_beg(1)
    DL.insert_at_beg(2)
    DL.insert_at_beg(3)
    DL.insert_at_last(10)
    DL.insert_at_last(20)
    DL.insert_at_last(30)
    DL.insert_at_last(40)
    DL.insert_at_pos(4,100)
    DL.insert_at_pos(8,100)
    DL.insert_at_pos(1,100)
    DL.insert_at_pos(9,500)
    DL.insert_at_pos(11,500)
    DL.insert_at_pos(13,500)
    # DL.delete_at_pos(4)
    DL.delete_at_pos(13)
    DL.view_list()