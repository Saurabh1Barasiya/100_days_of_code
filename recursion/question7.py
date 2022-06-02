# claim problem 
# n starte problem in
# ya to  1 sidi ya 2 sidi se hi ja sakte h ko possible no combination batao.

def nstair_possible_combination(nstair):
    if nstair == 0: 
        return 1
    if nstair < 0:
        return 0
    return nstair_possible_combination(nstair-1)+nstair_possible_combination(nstair-2)

print(nstair_possible_combination(5))
    
