# Rat in maze problem.


import numpy as np

def is_safe(new_x, new_y,N,visited,matrix):
    ''' is next move is possible or not. '''
    if (new_x >= 0 and new_x < N) and (new_y >= 0 and new_y < N) and (visited[new_x][new_y] == 0 ) and (matrix[new_x][new_y]==1):
        return True
    else:
        return False



def solve(matrix, visited, ans,output, start_x, start_y,N):
    # base case. 
    if start_x == N-1 and start_y == N-1:
        ans.append(''.join(output))
        return
    
    # mark visited.
    visited[start_x][start_y] = 1

    # now we have 4 choices - > Down,Left,Right,Up...


    # Down .
    new_x = start_x + 1
    new_y = start_y

    # check next move is possible or not...
    if is_safe(new_x, new_y,N,visited,matrix):
        # if move possible h to add kar do path. and recursive call.
        output.append("D")
        solve(matrix, visited, ans,output.copy(), new_x, new_y,N)
        output.pop()


    
    # Left .
    new_x = start_x 
    new_y = start_y - 1

    # check next move is possible or not...
    if is_safe(new_x, new_y,N,visited,matrix):
        # if move possible h to add kar do path. and recursive call.
        output.append("L")
        solve(matrix, visited, ans,output.copy(), new_x, new_y,N)
        output.pop()
        
    

    # Right .
    new_x = start_x 
    new_y = start_y + 1

    # check next move is possible or not...
    if is_safe(new_x, new_y,N,visited,matrix):
        # if move possible h to add kar do path. and recursive call.
        output.append("R")
        solve(matrix, visited, ans,output.copy(), new_x, new_y,N)
        output.pop()

    

    # Up .

    new_x = start_x - 1
    new_y = start_y

    # check next move is possible or not...
    if is_safe(new_x, new_y,N,visited,matrix):
        # if move possible h to add kar do path. and recursive call.
        output.append("U")
        solve(matrix, visited, ans,output.copy(), new_x, new_y,N)
        output.pop()
    
    visited[start_x][start_y] = 0


if __name__ == '__main__':
    N = 4
    matrix = [
        [1,0,0,0],
        [1,1,0,0],
        [1,1,0,0],
        [0,1,1,1]
    ]
    visited = np.zeros((4,4),dtype=int) # trap me na fase isiliye isko banaya.
    ans = output = []
    start_x = 0
    start_y = 0

    solve(matrix, visited, ans,output.copy(), start_x, start_y,N)
    print(ans)
    

