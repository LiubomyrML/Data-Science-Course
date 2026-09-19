import math

# Homework# 1
MONTHS_IN_YEAR = 12

name = input("Enter your Name: ")
monthly_salary = int(input("Enter your monthly salary: "))

print(f"{name}'s annual salary is {math.floor(monthly_salary * MONTHS_IN_YEAR / 1000)} thousand dollars!")



# Homework# 2
number = int(input("Enter a number: "))

print(number in range(100, 1000) and number % 2 == 0)



# Homework# 3
inputNumber = input("Enter a three digit number, that doesn't end in a zero: ")

if not int(inputNumber) in range(101, 1000):
    print("The number is not in the range!")
elif inputNumber.endswith("0"):
    print("Error: The number cannot end with a zero!")
else:
    print(int(inputNumber[::-1]))



#Homework# 4
firstWholeNumber = int(input("Enter the first whole number: "))
secondWholeNumber = int(input("Enter the second whole number: "))

print(f"Sum: {firstWholeNumber + secondWholeNumber}")
print(f"Difference: {firstWholeNumber - secondWholeNumber}")
print(f"Multiplication: {firstWholeNumber * secondWholeNumber}")
if secondWholeNumber == 0:
    print("Error: The number cannot be divided by zero!")
else:
    print(firstWholeNumber / secondWholeNumber)
    print(f"Remainder from Division: {firstWholeNumber % secondWholeNumber}")
print(firstWholeNumber >= secondWholeNumber)