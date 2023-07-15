# find minimum speaning tree using prims algorithem.

# ye code 100% sahi nahi h .

# 👀👀 Question 11 dekho.


import heapq
import sys

def print_adges_and_cost(res):
    """Print the adge list of MST"""

    total_cost = 0
    for item in res:
        nodes,cost = item
        total_cost += cost
        print(f"{nodes} --> {cost}")
        
    print(f"total cost is {total_cost}")

def make_adjust_list(edge,n):
    adj_list = {node:[] for node  in range(n)}

    for u,v,w in edge:
        adj_list[u].append((v,w))
        adj_list[v].append((u,w))

    return adj_list


# def get_min_key(key,mst):
#     mini = sys.maxsize
#     for i in range(n):
#         if mst[i] == False and key[i] < mini:
#             mini = key[i]
#             min_index = i
#     return min_index

def minimum_speaning_tree_prism(edges,n):
    adj_list = make_adjust_list(edges,n)

    # create a key array with n size with infine value.
    key = [sys.maxsize] * n

    # create a msg array with n size with false value.
    mst = [False] * n   

    # create a parent array with n size with None value.
    parent = [None] * n

    hq = []

    heapq.heappush(hq,(0,0))
    key[0] = 0
    
    parent[0] = -1

    for v in range(n):
        # u = get_min_key(key,mst)
        node,u = heapq.heappop(hq)
        # u = heapq.heappop(hq)

        # mark visit in mst 
        mst[u] = True

        store_list = adj_list[u]
        
        for next_node,weight in store_list:
            if mst[next_node] == False and weight < key[next_node]:
                key[next_node]= weight
                parent[next_node] = u
                heapq.heappush(hq,(weight,next_node))



    ans = []
    for i in range(1,n):
        pair = ((parent[i],i),key[i])
        ans.append(pair)
    
    return ans





if __name__ == '__main__':
    # edge = 3
    # node = 3

    edges = [
    [0, 1, 5],
    [1, 2, 3],
    [0, 2, 1]
    ]

    n = 3

    res = minimum_speaning_tree_prism(edges,n)

    print_adges_and_cost(res)



'''

GFG  practice.


class Solution:
    def get_min_key(self,key,mst,n):
        mini = sys.maxsize
        for i in range(n):
            if mst[i] == False and key[i] < mini:
                mini = key[i]
                min_index = i
        return min_index
    
    
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        n = V
        
        # create a key array with n size with infine value.
        key = [sys.maxsize] * n
    
        # create a msg array with n size with false value.
        mst = [False] * n   
    
        # create a parent array with n size with None value.
        parent = [None] * n
    
    
        key[0] = 0
        parent[0] = -1
        
        
        for v in range(n):
            u = self.get_min_key(key,mst,n)

            # mark visit in mst 
            mst[u] = True
    
            store_list = adj[u]
            
            for next_node,weight in store_list:
                if mst[next_node] == False and weight < key[next_node]:
                    key[next_node]= weight
                    parent[next_node] = u
                
        ans = 0
        for i in range(1,n):
            # pair = ((parent[i],i),key[i])
            ans += key[i]
        return ans
           
        


'''