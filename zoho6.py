def fizzBuzz(n):
    # Write your code here
    for i in range(n):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0 and i%3 != 3:
            print("Fizz")
        elif i%3 != 0 and i%5 != 5:
            print("Buzz")

