# sort a list [u,v,weight] using secound parameter weight.
# matlab list h uske ander multiple list h .
# or vo multiple list 2 elemet [u,v,weight] contain kar rahi h.

# hamko parent list ko sort karna h using weight.

def sort_using_weight(my_list):
    my_list.sort(key=lambda x: x[2] )

    # after sorting first value is u , secound value is v and last value is weight.

if __name__ == "__main__":
    # basiclly list has u,v,weight.
    # want to sort using  weight.
    my_list = [
        [1,2,2],
        [1,4,1],
        [1,5,4],
        [4,5,9],
        [4,3,5],
        [2,4,3],
        [2,3,3],
        [2,6,7],
        [3,6,8],
    ]

    sort_using_weight(my_list)

    # after sorting first value is u , secound value is v and last value is weight.
    for item in my_list:
        print(item)

