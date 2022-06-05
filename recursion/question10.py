# Search a element in an array using recursion.

def search_element(array,element):
    if len(array) == 0:
        return "Element not found in the Array"
    if array[0] == element:
        return f"Element : {array[0]} Element found in the Array"
    return search_element(array[1:],element)
ans = search_element(array=[1,2,3,4,5],element=0)
print(ans)
