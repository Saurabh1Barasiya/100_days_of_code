# initially all the nodes are independent.
# 1 2 3 4 5 6

# we need rank array and parent array.


# krushkal algorithem implment hui h yaha. 

# disjoin_set_Union_by_rank_and_path_comparession.

def find_parent(parent,node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent,parent[node])
    return parent[node]


def union_set(u,v,parent,rank):
    # get parent .
    u = find_parent(parent,u)
    v = find_parent(parent,v)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v]  = u
    else:
        # both are same kisi ko bhi kisi ka parent bana do but jo parent hoga,
        # uska rank increment kar dena.

        parent[v] = u
        rank[u] = rank[u] + 1


def mainimum_spannig_tree(edges,n):
    # create a rank array initilly 0 value with n size.

    rank = [0] * (n)
    

    # create a parent array initilly all nodes are aprent itself with n size.
    parent = [ node for node in range(n) ]
   

    # edge contain [u,v,weight] --> weight ke respect se sort  kar do.
    # edges.sort(key=lambda x:x[2])
    edges = sorted(edges,key=lambda x:x[2])

    min_weight = 0
   

    for u,v,weight in edges:
        u = find_parent(parent, u)
        v = find_parent(parent, v)
        
        if u != v:
            min_weight += weight
            union_set(u,v,parent,rank)
    
    return min_weight


if __name__ == '__main__':
    n = 4
    edges = [
            [0, 1, 10],
            [0, 2, 6],
            [0, 3, 5],
            [1, 3, 15],
            [2, 3, 4]

            # [1, 2, 6],
            # [2, 3, 5],
            # [3 ,4, 4],
            # [1 ,4, 1],
            # [1 ,3, 2],
            # [3 ,5, 3]

            # [0, 1, 3],
            # [0, 3, 5],
            # [1, 2, 1],
            # [2, 3, 8],


            # [1 ,2, 6],
            # [2 ,3, 2],
            # [1 ,3, 2],
            # [1 ,0, 2],


    ]
    
    ans = mainimum_spannig_tree(edges,n)
    print(ans)