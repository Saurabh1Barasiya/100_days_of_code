# find shortest path in undirected graph usng BFS.

from queue import Queue


def make_adjacency_list(edjes,n):
    adj_list = {node:set() for node in range(1,n+1)}
    
    # add all the directed edge to adjacency list
    for u,v in edjes:
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    # print(adj_list)
    return adj_list

def make_visited(n):
    visited = {node:False for node in range(1,n+1)}
    # print(visited)
    return visited

def get_shortest_path(edges,n,source,destination):
    adj_list = make_adjacency_list(edges,n)
    visited = make_visited(n)

    parent = {}

    q = Queue(maxsize=n)

    # first steap.
    q.put(source)
    visited[source] = True
    parent[source] = -1

    while not q.empty():
        front = q.get()  # remove and pop.

        store_list = adj_list[front]
        for node in store_list:
            if not visited[node]:
                visited[node] = True
                parent[node] = front
                q.put(node)
    

    # backtrack karke answer bana lo.
    ans = []
    current = destination
    ans.append(current)
    while source != current:
        current = parent[current]
        ans.append(current)
    ans.reverse()        
    
    # print(ans) #  valid answer.
    return ans

    
    


if __name__ == '__main__':
    edges = [
        [1, 2],
        [2, 1],
        [1, 3],
        [3, 1],
        [1, 4],
        [4, 1],
        [3, 8],
        [8, 3],
        [5, 2],
        [2, 5],
        [4, 6],
        [6, 4],
        [7, 6],
        [6, 7],
        [5, 8],
        [8, 5],
        [8, 7],
        [7, 8]
    ]

    n = 8
    source = 1
    destination = 8

    res = get_shortest_path(edges,n,source,destination)
    print(res)
   