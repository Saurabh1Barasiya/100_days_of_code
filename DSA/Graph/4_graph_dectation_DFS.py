# cycle dectection using DFS.

def make_adjancy_list(n,edge):
    adj_list = {}
    for i in range(n):
        adj_list[i] = []
    
    for u,v in edge:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list
    
def is_cycle_utils_dfs(node,parent,adj_list,visited):  
    visited[node] = True
    store_list = adj_list[node]
    for neighbor in store_list:
        if not visited[neighbor]:
            res = is_cycle_utils_dfs(neighbor,node,adj_list,visited)
            return res
        else:
            # yaha aaye ho matlab visited true h bas 1 condition or check kar lo.
            if neighbor != parent:
                return True
    return False
            

def is_cycle(edge,n):
    # is question me hame 1 parent ki need bhi padegi .
    # to recursion ka use kar lege alag se  data structure lene ki need nahi h parent ke liye 
    # initial node ke liye parent ki value -1 set kar dege.

    adj_list = make_adjancy_list(n,edge)
    visited = {i:False for i in range(n)}
    parent = -1
    
    for i in range(n):
        if not visited[i]:
            res = is_cycle_utils_dfs(i,parent,adj_list,visited)
            
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

    is_cycle(edge,n)
    
