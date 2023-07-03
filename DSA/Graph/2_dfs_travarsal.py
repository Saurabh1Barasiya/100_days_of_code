def make_adj_list(edge,vertax,n):
    adj_list = {}
    for i in range(n):
        # adj_list[i]=[]
        adj_list[i]=set()
    

    for data in edge:
        # as we know its undirected graph.
        if len(data) == 2:
            u = data[0]
            v = data[1]
            adj_list[u].add(v)
            adj_list[v].add(u)
            # adj_list[u].append(v)
            # adj_list[v].append(u)
        else:
            # if single element hota to issue hota.
            pass
    
    return adj_list

def dfs_utils(adj_list,visisted,ans,node):
    ans.append(node)
    visisted[node] = True

    store_list = adj_list[node]
    for node in store_list:
        if not visisted[node]:
            dfs_utils(adj_list,visisted,ans,node)

def dfs(edge,vertax,n):
    adj_list = make_adj_list(edge,vertax,n)
    # print(adj_list)

    # make a visited map.
    visisted = {x : False for x in range(n)}
    
    for i in range(len(vertax)):
        if not visisted[i]:
            dfs_utils(adj_list,visisted,ans,i)

if __name__ == '__main__':
    edge = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 3],
        [2, 4],
        [3, 5],
        [3, 6],
        [4, 7],
        [4, 5],
        [5, 2],
    ]

    vertax = [0,1,2,3,4,5,6,7]
    n = len(vertax)
    ans = []
    dfs(edge,vertax,n)
    print(ans)