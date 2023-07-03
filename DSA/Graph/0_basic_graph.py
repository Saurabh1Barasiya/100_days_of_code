# graph represation.
def get_matrix(n):
    mat = []
    for row in range(n):
        temp = []
        for col in range(n):
            temp.append(0)
        mat.append(temp)
    return mat

def build_graph(ipt,n):
    matrix = get_matrix(n)
    # print(matrix)

    for u,v in ipt:
        matrix[u][v] = 1
        matrix[v][u] = 1
    
    return matrix

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col],end=" ")
        print("")

def get_ajd_list(ipt,n):
    graph_dict = {}
    for i in range(n):
        graph_dict[i] = []

    # print(graph_dict)
    for u,v in ipt:
        graph_dict[u].append(v)
        graph_dict[v].append(u)
    
    for key,val in graph_dict.items():
        print(f"{key} : {val}")

if __name__ == "__main__":
    n = 4
    ipt = [
        [0,1],
        [0,2],
        [1,3],
        [2,3],
    ]


    res = build_graph(ipt,n)
    
    print("The Adjacency matrix")
    print_matrix(res)

    print("The Adjacency List")
    get_ajd_list(ipt,n)