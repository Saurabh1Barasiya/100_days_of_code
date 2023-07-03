from collections import deque

def make_adjacency_list(edjes,n):
    adj_list = {node:[] for node in range(1,n+1)}
    
    # add all the directed edge to adjacency list
    for u,v in edjes:
        adj_list[u].append(v)
    
    return adj_list

def make_visited(n):
    visited = {node:False for node in range(1,n+1)}
    return visited
            

def topological_dfs_utils(node,adj_list,visited,stack):
    visited[node] = True
    store_list  = adj_list[node]
    for neighbor in store_list:
        if not visited[neighbor]:
            topological_dfs_utils(neighbor,adj_list,visited,stack)
    
    stack.append(node)


def get_topological_order(edjes,n):
    stack = deque()  #LIFO order.
    adj_list=make_adjacency_list(edjes,n)
    visited=make_visited(n)
    ans = []
    
    for i in range(1,n+1):
        if not visited[i]:
            topological_dfs_utils(i,adj_list,visited,stack)
    
    while stack:
        ans.append(stack.pop())

    return ans

if __name__ == "__main__":
    edjes = [
        [1,2],
        [1,3],
        [2,4],
        [3,4],
        [4,5],
        [4,6],
        [5,6],
    ]
    n = 6
    res = get_topological_order(edjes,n)
    print(res)
























# from collections import deque
# stack = deque()
# stack.append(6)
# stack.append(5)
# stack.append(4)
# stack.append(2)
# stack.append(3)
# stack.append(1)

# while stack:
#     print(stack.pop(),end=" ")