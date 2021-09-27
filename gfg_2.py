'''
1 2 3 4 5 6 
Reversed array is 
6 5 4 3 2 1 
'''

def rev(A,start_ind,end_ind):
    i = 0
    while i <3:
        if A[i] < A[len(A)-1]:
            A[i],A[end_ind] = A[end_ind],A[start_ind]
            start_ind += 1
            end_ind += 1    
        i += 1

A = [1,2,3,4,5,6]
rev(A,0,5)
print(A)

