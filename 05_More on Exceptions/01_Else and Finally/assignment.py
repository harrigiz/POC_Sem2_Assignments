number1 = 0
number2 = 0
try:
    number1 = int(input("Enter an integer:"))
    number2 = int(input("Enter another integer:"))
except ValueError:
    print("No integer entered :/")
else:
    print("No value error detected")
finally:
    print("Values taked care of")

answer = number1 / number2

try:
    number1 / number2 == answer 
    print(answer), ('Here is your answer!')

except ZeroDivisionError:
    print('division by zero is not possible.')
else:
    print("No value error detected")
finally:
    print("Values taked care of")
