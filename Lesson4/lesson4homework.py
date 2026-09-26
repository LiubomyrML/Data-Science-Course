# HomeWork #1
number = int(input("Please enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("ham")
elif number % 3 == 0:
    print("foo")
elif number % 5 == 0:
    print("bar")


# HomeWork #2
first_number = float(input("Please enter your first number: "))
second_number = float(input("Please enter your second number: "))

if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
elif first_number == second_number:
    print("Both numbers are equal!")
else:
    print(f"{second_number} is greater than {first_number}")


# HomeWork #3
number_one = float(input("Please enter your first number: "))
number_two = float(input("Please enter your second number: "))
number_three = float(input("Please enter your third number: "))

numbers = [number_one, number_two, number_three]

# I used Max and Min for learning purpose.
largest = max(numbers)
smallest = min(numbers)

medium = sorted(numbers)[1]

print(f"Largest: {largest}")
print(f"Medium: {medium}")
print(f"Smallest: {smallest}")


# HomeWork #4
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# HomeWork #5
for num in range(1, 101):
    if num % 7 == 0 or '7' in str(num):
        print("BOOM!")
    else:
        print(num)