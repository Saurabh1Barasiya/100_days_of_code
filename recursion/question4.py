# number = > 412
# output => four one two.

l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# using loop
# num_string = input("Enter number")
# for i in num_string:
#     print(l1[int(i)], end=' ')


# using recursion

def print_text(number):
    if number == 0:
        return 
    else:
        last_digit = number % 10
        number = number // 10 #  small number.
        print_text(number)
        print(l1[last_digit])

num = int(input("Enter number"))
print_text(num)
