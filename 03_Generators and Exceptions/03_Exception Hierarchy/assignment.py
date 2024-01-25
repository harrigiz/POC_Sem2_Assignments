number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
except ValueError:
    print('No integer entered :/')

answer = number1 / number2

try:
    number1 / number2 == answer 
    print(answer), ('Here is your answer!')

except ZeroDivisionError:
    print('division by zero is not possible.')
    