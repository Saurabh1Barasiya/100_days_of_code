# reverse k group linklist 
# i/p ---->  100 200 300 400 500 600 
# o/p ---->  200 100 400 300 600 500

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
        
   
    def reverse_list(self):
        prev = None
        curr = self.start
        forword = None
        while curr != None:
            forword = curr.next
            curr.next = prev
            prev = curr
            curr = forword
        self.start = prev

    def getlength(self,head):
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count


    def rev(self,head,k):
        if head == None:
            return None
        
        forword = None
        curr = head
        prev = None

        length = self.getlength(head)

        if length < k:
            return head

        count = 0
        while curr != None and count < k:
            forword = curr.next
            curr.next = prev
            prev = curr
            curr = forword
            count += 1
        
        if forword != None:
            head.next = self.rev(forword,k)

        return prev
        

    def reverse_k_group(self,k):
        head = self.start
        prev = self.rev(head, k)      
        self.start = prev

    

my_list = Linklist()

# my_list.inser_at_last(100)
# my_list.inser_at_last(200)
# my_list.inser_at_last(300)
# my_list.inser_at_last(400)
# my_list.inser_at_last(500)



my_list.inser_at_last(1)
my_list.inser_at_last(2)
my_list.inser_at_last(3)
my_list.inser_at_last(4)
my_list.inser_at_last(5)


# [1,2,3,4,5]
# 3
# my_list.inser_at_last(600)


my_list.view_data()
print("\n")
my_list.reverse_k_group(3)

my_list.view_data()





'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self,head):
        temp = head
        c = 0
        while temp:
            c+=1
            temp = temp.next
        return c
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        
        forword = None
        curr = head
        prev = None
        count = 0
        
        length = self.get_length(head)
        
        if length < k:
            return head
        
        
        while curr != None and count < k:
                forword = curr.next
                curr.next = prev
                prev = curr
                curr = forword
                count += 1
        
        if forword != None:
                head.next = self.reverseKGroup(forword,k)
            
        return prev
'''
