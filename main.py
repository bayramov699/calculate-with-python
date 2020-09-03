import math

print("Hello, this is very basic calculator.")

name = input("Hello, please input your name:")



number1 = input("Dear," + name + ",please input first number:")
operator = input("Please choose operation type (Example:+,-,/,*):")
number2 = input("Dear," + name + ", please input second number:")

number1 = int(number1)
number2 = int(number2)

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2

print("Dear," + name + ", your result is equal to" + str(result))