# a = 10
# b = 20

# a **= 5

# print(a)


hobbies = ["Swimming", "Programming", "Teaching", "Soccer", "Football"] # list
word_list = ["I", "Love", "Python", "Very", "Much", "!"]
reverseSentence = ["!", "Python", "Love", "I"]
numbers = [24, 68, 12, 3, 89, 99, 39, 0]

#hobbies.append("Hiking")   Only adds one Element to the List.
#hobbies.append("Running")  Only adds one Element to the List.
#hobbies.append("Gym")      Only adds one Element to the List.
hobbies.extend(["Hiking", "Running", "Gym"]) # It takes the existing List, and extends it with new Elements that are provided.


print(hobbies[0:2])
print(f"Numbers: {numbers[2:6]}") # Elements near each other.
print(numbers[::2]) # Skipping.
print(numbers[-1]) # The Last Element.

print(word_list[-1:-4:-1]) # Reverse From a specific Element of the List.
print(reverseSentence[::-1]) # Reverse From The Back of the List to the Front.


print("Football" in hobbies) # Checks if hobbies contain the word Football.
print(12 in numbers) # Checks if numbers List contains number 12.


if "Programming" in hobbies and "Swimming" in hobbies:
    print("I Love that Hobbies too!")
elif 3 in numbers:
    print("I have that number too!")
else:
    print("I Don't Have the same Answer!")


Hobby = True if "Soccer" in hobbies and "Football" in hobbies else False
print(Hobby)


# print(numbers[0])
# print(numbers[1])
# print(numbers[2])


even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)
print(len(even))
print(len("Banana")) # Shows the Length on the Word Banana


fruit = "APPLE"
print(fruit.lower()) # Converts the String to Lower Case.


goods = ["apple", "banana", "cherry"]

for good in goods:
    print(good.upper()) # Prints every element in Upper Case.


meats = [["Pork", "Chicken"],["Beef", "Sheep"]]

print(meats[1][1])
print(meats[1].index("Beef")) # Index of the Word Beef in Meats List.


result = 0 # Sum of the Numbers List

for number in numbers:
    result += number

print(result)


for word in hobbies:
    print(word)


sentence = "I! Love. Python!"
print(sentence[::-1])
print(len(sentence))
print(sentence.split(".")) # Splits the sentence after it sees a dot.
print(sentence.replace("!", ".").split(". ")) # It replaces "!", to a dot, and then when it sees a dot, it splits the sentence, and creates new Elements in the List.