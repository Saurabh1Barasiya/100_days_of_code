# So here we code how to decited cycle in Dircted Graph using DFS.

def make_adj_list(edges,n):
    # because mere paas node 1 se start ho rahe h to me loop 1 se n tak chalunga.

    # adj_list = {}
    # for i in range(1,n):
    #     adj_list[i] = []
    
    adj_list = {node : [] for node in range(1,n+1)}
    
    for  u,v in edges:
        adj_list[u].append(v)
    
    # print(adj_list)
    return adj_list

def make_visited_array_or_map(n):
    visited = {node:False for node in range(1,n+1)}
    return visited

def make_visited_dfs_array_or_map(n):
    visited_dfs = {node:False for node in range(1,n+1)}
    return visited_dfs


def is_cycle_utis(node,visited,visited_dfs,adj_list):
    visited[node] = True
    visited_dfs[node] = True
    
    store_list = adj_list[node]

    for neighbor in store_list:
        if not visited[neighbor]:
            res = is_cycle_utis(neighbor,visited,visited_dfs,adj_list)
            if res:
                return True
        else:
            # yaha aaye ho matlab visitd  to h to 1 condition or check kar lo ki visited_dfs bhi true ho.

            # 1 kaam karne dono condition check kar lete h.
            if visited[neighbor] and visited_dfs[neighbor]:
                return True
    visited_dfs[node] = False
    return False  #optional h 


def is_cycle(n):
    adj_list = make_adj_list(edges,n)
    visited = make_visited_array_or_map(n)
    visited_dfs = make_visited_dfs_array_or_map(n)
    
    for src in (1,n+1):
        if not visited[src]:
            ans = is_cycle_utis(src,visited,visited_dfs,adj_list)
            if ans:
                return True
    return False

if __name__ == '__main__':
    edges = [
        [1,2],
        [2,3],
        [2,4],
        [3,7],
        [3,8],
        [8,7],
        [4,5],
        [5,6],
        [6,4],


        # [1,2],
        # [2,3],
        # [3,1],
        # [2,4],



        # [1,2],
        # [1,3],
        # [3,4],
        # [4,2],
    ]

    n = len(edges)
    # print(n)
    ans = is_cycle(n)
    if ans:
        print("Yes cycle is present in the graph")
    else:
        print("No cycle is not present in the graph")


    
