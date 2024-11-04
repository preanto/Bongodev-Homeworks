
# Write a Python program that takes a single integer n as input from the user. The program should output:
# "Fizz" if n is a multiple of 3.
# "Buzz" if n is a multiple of 5.
# "FizzBuzz" if n is a multiple of both 3 and 5.
# • Otherwise, output not a FizzBuzz number.

a = int(input("Enter a Number: "))
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
else:
    print("output not a FizzBuzz number.")