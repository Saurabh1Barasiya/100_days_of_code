# build simple tree and travarsal.
# inorder , perorder , postorder.


from queue import Queue
class Node:
    '''IT will create a node.'''
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def build_Tree(root):
    data = int(input("Please enter the data : "))
    root = Node(data)

    if data == -1:
        return None
    
    print(f"Enter the data for inserting in left of {data}")
    root.left = build_Tree(root.left)

    print(f"Enter the data for inserting in right of {data}")
    root.right = build_Tree(root.right)

    return root

def leval_order_traversal(root):
    q = Queue(100)
    q.put(root)
    q.put(None)
    while not  q.empty():
        temp = q.get()
        if temp == None:
            print()
            if not q.empty():
                q.put(None)
        else:
            print(temp.data,end=" ")
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)

def in_order_travarsal(root):
    #  L O R
    if root == None:
        return
    
    in_order_travarsal(root.left)  # l
    print(root.data,end=" ")       # O
    in_order_travarsal(root.right) # R


def pre_order_travarsal(root):

    if root == None:
        return
    
    print(root.data,end=" ")        # O
    pre_order_travarsal(root.left)  # L
    pre_order_travarsal(root.right) # R


def post_order_travarsal(root):
    if root == None:
        return 
    
    post_order_travarsal(root.left)   # L
    post_order_travarsal(root.right)  # R
    print(root.data,end=" ")          # O


if __name__ == '__main__':
    root = None

    root = build_Tree(root)
    print("\n leval order travarsal")
    leval_order_traversal(root)

    print("\n In order travarsal")
    in_order_travarsal(root)

    print("\n Pre order  travarsal")
    pre_order_travarsal(root)

    print("\n Post order travarsal")
    post_order_travarsal(root)



    