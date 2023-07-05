# find shortest path from source to all node in undirected graph.

import sys

def make_adjacent_list(edges,n):
    adj_list = {node:[] for node in range(n)}
    
    # undirected graph h.
    # node , next_node , weight.
    for u,v,w in edges:
        # pair = (node,weight)
        adj_list[u].append((v,w))
        adj_list[v].append((u,w))
    
    # print(adj_list)
    # for key,value in adj_list.items():
    #     print(key,value)

    return adj_list

def dijkstra_shortest_path(edges,source,n):
    s = set()
    distance = [sys.maxsize] * n

    adj_list = make_adjacent_list(edges,n)

    s.add((0,source))

    distance[source] = 0

    while s:
        # jab bhi set se value nikaloge to vo minimum hi honi chahiye.
        # value nikal kar , set se turent delete kar dena.
        
        top = min(s)
        s.discard(top)
       
        current_distance = top[0]
        current_node = top[1]

        store_list = adj_list[current_node]

        for next_node , weight in  store_list:
            if current_distance + weight < distance[next_node]:
                pair = (distance[next_node],next_node)

                # dalne se pahle check kar lena if node corresponding koi entry h to usko delete kar  dena.
                if pair in s:
                    s.discard(pair)
                
                # update the distanse array.
                distance[next_node] = current_distance + weight

                new_pair = (distance[next_node],next_node)

                s.add(new_pair)
    
    return distance



if __name__ == '__main__':
    edges = [
        [0, 1, 4],
        [0, 7, 8],
        [1, 2, 8],
        [1, 7, 11],
        [2, 3, 7],
        [2, 8, 2],
        [2, 5, 4],
        [3, 4, 9],
        [3, 5, 14],
        [4, 5, 10],
        [5, 6, 2],
        [6, 7, 1],
        [6, 8, 6],
        [7, 8, 7]
    ]

    source = 0
    n = 9
    
    ans = dijkstra_shortest_path(edges,source,n)

    for i in ans:
        print(i)