from ast import Return


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


def merge_two_sorted_linklist(left, right):
    if left == None:
        return right
    if right == None:
        return left

    dummy = Node(-1)
    tail = dummy

    while left != None and right != None:
        if left.data < right.data:
            tail.next  = left
            tail = left
            left = left.next
        else:
            tail.next = right
            tail = right
            right = right.next
    
    while left != None:
        tail.next = left
        tail = left
        left = left.next

    while right != None:
        tail.next = right
        tail = right
        right = right.next
    
    merged = dummy.next

    return merged

def get_middle_node(head):
    
    temp = head
    slow = temp 
    fast = slow.next

    while fast != None and fast.next != None:
        fast = fast.next
        fast = fast.next
        slow = slow.next
    print("middle Node ka data ---> : ", slow.data)
    return slow 


def merge_link(head):

    if head == None or head.next == None:
        return head
    
    middle_node = get_middle_node(head)
    # temp = head
    left = head
    right = middle_node.next
    middle_node.next = None

    left = merge_link(left)
    right = merge_link(right)

    result = merge_two_sorted_linklist(left, right)

    return result


first = Linklist()


first.inser_at_last(1)
first.inser_at_last(9)
first.inser_at_last(11)
first.inser_at_last(5)
first.inser_at_last(2)
first.inser_at_last(6)
first.inser_at_last(100)
first.inser_at_last(50)



merged = merge_link(first.start)

while merged:
    print(merged.data , end=" ")
    merged = merged.next
