# Write a calculator program that takes three inputs from the user:
# 1. Input1: A number (float or integer).
# 2. Input2: A number (float or integer).
# 3. Operator: A character representing a mathematical operation. The operator can be one of the following: +, -, *, /, or %.
# The program should perform the following tasks:
# ⚫ Validate the inputs to ensure that Input1 and Input2 are valid numbers and that the Operator is one of the specified characters.
# Use conditional statements to determine which operation to perform based on the Operator provided.
# • If the operator is +, return the sum of Input1 and Input2.
# • If the operator is -, return the difference between Input1 and Input2.
# • If the operator is *, return the product of Input1 and Input2.
# ⚫ If the operator is, return the quotient of Input1 divided by Input2. If Input2 is zero,
# return an appropriate error message indicating that division by zero is not allowed.
# • If the operator is %, return the remainder of Input1 divided by Input2.
# • Display the result of the operation to the user.
# Example Input/Output:
# 1. Input: Input1 = 10, Input2 = 5, Operator = + Output: The result is 15
# 2. Input: Input1 = 10, Input2 = 0, Operator = / Output: Error: Division by zero is not allowed.

a = float(input("Input1 = "))
b = float(input("Input2 = "))
o = str(input("Operator (+,-,*,/,%): "))
if o == '+':
    print("The result is: ", a+b)
elif o == '-':
    print("The result is: ", a-b)
elif o == '*':
    print("The result is: ", a*b)
elif o == '/':
    try:
        x = a/b
        print("The result is: ", x)
    except:
        print("Error: Division by zero is not allowed")

        