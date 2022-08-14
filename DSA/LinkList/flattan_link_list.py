'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None      
'''


def mergeList(first,secound):
    if first == None:
        return secound
    if secound == None:
        return first
        
    head = None
    tail = None
    
    while first != None and secound != None:
        if head == None:
            if first.data < secound.data:
                head = first
                tail = first
                first = first.bottom
            else:
                head = secound
                tail = secound
                secound = secound.bottom
        else:
            if first.data < secound.data:
                tail.bottom = first
                first = first.bottom
                tail = tail.bottom
            else:
                tail.bottom = secound
                secound = secound.bottom
                tail = tail.bottom
                
                
    if first:
        tail.bottom = first
    if secound:
        tail.bottom = secound

    return head


def flatten(root):
    #Your code here
    if root==None or root.next==None:
        return root
        
    forword = root.next
    remaning = flatten(forword)
    
    return mergeList(root,remaning)
