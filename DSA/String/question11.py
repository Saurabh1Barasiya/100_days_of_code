# A Python program to print all
# permutations using library function
from itertools import permutations
'''
# Get all permutations of [1, 2, 3]
perm = permutations("ab")

# Print the obtained permutations
for i in list(perm):
  print (i)

'''

# Permutation in string.

def check_permutation(original_string,per):
    return per in original_string

if __name__ == '__main__':
    l1 = []
    s = "ab"
    Original = "eidabooo"
    # Original = "eidboaoo"
    perms = permutations(s)
    for i in list(perms):
        per = "".join(i)
        l1.append(check_permutation(Original,per))
    print(any(l1))