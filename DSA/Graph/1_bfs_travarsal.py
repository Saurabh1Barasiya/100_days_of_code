from queue import Queue

def make_adj_list(edges,n):
    adj_list = {}
    for i in range(n):
        adj_list[i]=[]

    for data in edges:
        # as we know its undirected graph.
        if len(data) == 2:
            u = data[0]
            v = data[1]
            adj_list[u].append(v)
            adj_list[v].append(u)
        else:
            pass
    
    return adj_list


def bfs_utils(adj_list,visisted,ans,node):
    q = Queue(maxsize=len(visisted))
    q.put(node)
    while (not q.empty()):
        front_node = q.get() # return and remove from queue.

        # store in ans array.
        ans.append(front_node)

        stor_list = adj_list[front_node]

        for node in  stor_list:
            if not visisted[node]:
                q.put(node)
                visisted[node] = True


def bfs(vertex,edges,ans,n):
    # 1. make adjancy list
    adj_list = make_adj_list(edges,n)
    print(adj_list)

    # make a visited map.
    visisted = {x : False for x in range(n)}

    for i in range(len(vertex)):
        if not visisted[i]:
            bfs_utils(adj_list,visisted,ans,i)


if __name__ == '__main__':
    n = 4
    ipt = [
        [0,1],
        [0,2],
        [1,3],
        [2,3],


        # [0, 1],
        # [0, 2],
        # [1, 2],
        # [2, 0],
        # [2, 3],
        # [3, 3],

        # [1,0],
        # [1,3],
        # [0,3],
        # [2]
    ]
    ans = []
    vertex = [0,1,2,3]
    bfs(vertex,ipt,ans,n)
    print(ans)