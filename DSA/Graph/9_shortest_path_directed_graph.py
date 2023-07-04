# Shortest path in direct acyclic graph. har node se har node ka shortest path nikalo.

from collections import deque
import sys

def make_adjcent_list(edges,n):
    adj_list = {node:[] for node in range(n)}
    
    # ek node se dusre node jane ka weight diya hua h .

    # node , next_node , weight.
    # u    ,  v        , w.
    for u,v,w in edges:
        pair = [v,w]
        adj_list[u].append(pair)
    
    # printing the adjasent list.
    # for key , value in adj_list.items():
    #     print(f"{key} ==> {value}")

    return adj_list

def get_visited(n):
    visited = {node:False for node in range(n)}
    return visited
    
def get_topological_odering(src,adj_list,stack,visited):
    visited[src] = True
    store_list = adj_list[src]
    for node in store_list:
        next_node = node[0]
        if not visited[next_node]:
            get_topological_odering(next_node,adj_list,stack,visited)
    
    # bapas jate hue node par value daal dena.
    stack.append(src)
    

def get_shortest_path(edges,n,source_node):
    adj_list = make_adjcent_list(edges,n)
    visited = get_visited(n)
    stack = deque()   # store logical order.

    # get topological order 
    for i in range(n):
        if not visited[i]:
            get_topological_odering(i,adj_list,stack,visited)

    # make a distance array with infine value with n element.
    distance = [sys.maxsize] * n
   
    distance[source_node] = 0
    

    while stack:
        top = stack.pop()  # pop and return.
        if distance[top] != sys.maxsize:
            store_list = adj_list[top]
            for next_node,weight in store_list:
                if distance[top] + weight < distance[next_node]:
                    distance[next_node] = distance[top] + weight
    print(distance)

if __name__ == "__main__":
    edges = [
    [1, 3, 6],
    [1, 2, 2],
    [0, 1, 5],
    [0, 2, 3],
    [3, 4, -1],
    [2, 4, 4],
    [2, 5, 2],
    [2, 3, 7],
    [4, 5, -2],
    ]

    n = 6
    source_node  = 1
    get_shortest_path(edges,n,source_node)