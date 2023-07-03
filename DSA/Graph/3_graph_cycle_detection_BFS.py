# cycle dectection using BFS.


from queue import Queue

def make_adjancy_list(n,edge):
    adj_list = {}
    for i in range(n):
        adj_list[i] = []
    
    for u,v in edge:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list
    
def is_sycle_utils(src,adj_list,visited,parent,n):
    q = Queue(maxsize=n)

    parent[src] = -1
    visited[src] = True
    q.put(src)
    
    while not q.empty():
        front = q.get()  # remove and return .
        
        store_list = adj_list[front]
        for neighbour in store_list:
            if visited[neighbour] and neighbour != parent[front]:
                return True
            else:
                if not visited[neighbour]:
                    q.put(neighbour)
                    visited[neighbour] = True
                    parent[neighbour] = front
    return False

        
def is_sycle(edge,n):
    # is question me hame 1 parent ki need bhi padegi .

    adj_list = make_adjancy_list(n,edge)
    visited = {i:False for i in range(n)}
    parent = {}
    
    for i in range(n):
        if not visited[i]:
            res = is_sycle_utils(i,adj_list,visited,parent,n)
            
    if res:
        print("Cycle found in Graph")
    else:
        print("Cycle Not found in Graph")


if __name__ == "__main__":
    n = 5
    edge = [
        [1, 0],
        [1, 2],
        [2, 0],
        [0, 3],
        [3, 4]
    ]

    is_sycle(edge,n)
    

