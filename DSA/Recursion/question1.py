# print digit like 412 --> four one two. using Recursion.
def print_dight(number,arr):
    if number == 0:
        return
    else:
        last_digit = number % 10
        number = number // 10
        print_dight(number,arr)
        print(arr[last_digit])

if __name__ == '__main__':
    n = 431
    arr = ["zero", "one", "two", "three", "four","five","six","seven","eight","nine"]
    print_dight(n,arr)
