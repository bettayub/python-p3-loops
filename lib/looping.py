# happyNewYear() function
def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

happy_new_year()
print()

# fizzbuzzPrinter() and fizzbuzz() functions
def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

fizzbuzz_printer()
print()

# reverseString() function
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = input("Enter a string: ")
reversed_input = reverse_string(input_string)
print("Reversed string:", reversed_input)
print()

# square_integers() function
def square_integers(int_list):
    return [num ** 2 for num in int_list]

input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
squared_list = square_integers(input_list)
print("Squared integers:", squared_list)
