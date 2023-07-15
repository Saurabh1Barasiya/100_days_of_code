# find bridges in a graph. 


def make_adjcent_list(edges,n):
    adj_list = {node:[] for node in range(n)}
    
    # add all the nodes to their respective adjacency lists
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list

def make_visited(n):
    visited = {node:False for node in range(n)}
    return visited

def find_bridges_utils(node,parent,visited,adj_list,timer,low,disc):
    low[node]=disc[node] = timer 
    visited[node] = True
    timer += 1

    store_list = adj_list[node]
    for neighbor in store_list:
        if  neighbor == parent:
            continue

        if not visited[neighbor]:
            find_bridges_utils(neighbor,node,visited,adj_list,timer,low,disc)
            low[node] = min(low[node],low[neighbor])

            # check bridge.
            if low[neighbor] > disc[node]:
                print(f"bridge found {node} -- {neighbor}   ")
        else:
            low[node] = min(low[node],disc[neighbor])
        



def find_bridges(edge,n):
    adj_list = make_adjcent_list(edge,n)
    visited = make_visited(n)

    timer = 0
    low = [0] * n
    disc = [0] * n

    for i in range(n):
        if not visited[i]:
            find_bridges_utils(i,-1,visited,adj_list,timer,low,disc)
    
if __name__ == "__main__":
    edges = [
        # [1, 0],
        # [0, 2],
        # [2, 1],
        # [0, 3],
        # [3, 4],


        # [0, 1],
        # [1, 2],
        # [2, 0],
        # [1, 3],
        # [1, 4],
        # [1, 6],
        # [3, 5],
        # [4, 5]


        # [0, 1],
        # [1, 2],
        # [2, 3]



        # [1,2],
        # [1,0],
        # [2,0],
        # [0,4],
        # [4,5],
        # [4,3],
        # [5,3]

        [0,1],
        [0,2],
        [0,3],
        [1,2],
        [3,4],
    
    ]
    # n = 5
    # n = 7
    n = 5


    find_bridges(edges,n)






'''

Question ------>             1192. Critical Connections in a Network.


class Solution:
    def make_adj(self,connections,n):
        adj_list = {node:[] for node in range(n)}

        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        return adj_list
    
    def criticalConnections_utils(self,node,parent,timer,low,disc,visited,adj_list,ans):
        visited[node] = True
        low[node]=disc[node]=timer
        timer+=1

        store_list = adj_list[node]
        for neighbour in store_list:
            if neighbour == parent:
                continue
            if not visited[neighbour]:
                self.criticalConnections_utils(neighbour,node,timer,low,disc,visited,adj_list,ans)
                low[node] = min(low[node],low[neighbour])

                # check if there is a edge.
                if low[neighbour] > disc[node]:
                    ans.append([node,neighbour])

            else:
                # back edge wala formula.
                low[node] = min(low[node],disc[neighbour])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list =  self.make_adj(connections,n)
        visited = [False] * n

        low = [0] * n
        disc = [0] * n
        parent = -1
        timer = 1
        ans = []

        for i in range(n):
            if not visited[i]:
                self.criticalConnections_utils(i,parent,timer,low,disc,visited,adj_list,ans)
        return ans


'''