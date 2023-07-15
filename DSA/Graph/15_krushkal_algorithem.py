# ye code utna sahi ni h 

# ans to aa jayega but dont follow.

# question 14 ka solution dekho.

'''

def find_parent(parent,node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent,parent[node])
    return parent[node]


def union_set(u,v,parent,rank):
    # get parent .
    p1 = find_parent(parent,u)
    p2 = find_parent(parent,v)

    if rank[p1] < rank[p2]:
        parent[u] = v
    elif rank[p2] < rank[p1]:
        parent[v]  = u
    else:
        # both are same kisi ko bhi kisi ka parent bana do but jo parent hoga,
        # uska rank increment kar dena.

        parent[v] = u
        rank[u] = rank[u] + 1


def mainimum_spannig_tree(edges,n):
    # create a rank array initilly 0 value with n size.

    rank = [0] * (n+1)
    rank[0] = None

    # create a parent array initilly all nodes are aprent itself with n size.
    parent = [ node for node in range(n+1) ]
    parent[0] = None

    # edge contain [u,v,weight] --> weight ke respect se sort  kar do.
    # edges.sort(key=lambda x:x[2])
    edges = sorted(edges,key=lambda x:x[2])

    min_weight = 0
   
    count = 0
    for u,v,weight in edges:
        
        x = find_parent(parent, u)
        y = find_parent(parent, v)
        
        if x != y:
            min_weight += weight
            count += 1
            union_set(u,v,parent,rank)
    
    # return min_weight,count
    return min_weight





if __name__ == '__main__':
    n = 2
    edges = [

            [1 ,2, 4]

            # [0, 1, 10],
            # [0, 2, 6],
            # [0, 3, 5],
            # [1, 3, 15],
            # [2, 3, 4]

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

            # [1, 2, 1],
            # [2, 3, 2],
            # [3, 1, 3],


            # [1 ,2, 4],
            # [2 ,3, 5],
            # [3 ,4, 1],
          


    ]
    
    ans = mainimum_spannig_tree(edges,n)
    print(ans)
'''