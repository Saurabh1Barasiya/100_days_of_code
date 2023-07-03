from queue import Queue

def make_adj_list(edges,v):
    adj = {}
    for i in range(1,v+1):
        adj[i] = []
    

    for u,v in edges:
        adj[u].append(v)
    
    return adj
    
def make_indegree(adj_list,v):
    indegree = {node:0 for node in adj_list.keys()}
    
    for node,store_list in adj_list.items():
        for neighbor_node in store_list:
            indegree[neighbor_node] += 1
    # print(indegree)
    return indegree

def topological_sort(edges,v,e):
    ans = []

    # steap 1.
    adj_list = make_adj_list(edges,v)

    # steap 2. make Indegree.
    in_degrees = make_indegree(adj_list,v)

    # make a queue.
    q = Queue(maxsize=v)

    # put all the node in a queue thats has indrgree == 0.
    for i in range(1,v+1):
        if in_degrees[i] == 0:
            q.put(i)

    # now do BFS.
    while not q.empty():
        front = q.get() # return and pop from queue.
        ans.append(front) #
        store_list = adj_list[front]
        
        for neighbor in store_list:
            # delete node means decrement the indegree.
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                q.put(neighbor)

    print(ans)

    
    
    

if __name__ == '__main__':
    edges = [
        [1,2],
        [1,3],
        [2,5],
        [3,5],
        [5,4],
    ]

    v = 5
    e = 5

    topological_sort(edges,v,e)    