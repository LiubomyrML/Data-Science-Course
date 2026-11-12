# from Lesson5 import lesson5_module
from Python.Lesson5.Lesson5_package.lesson5_module import concat_all_strings as con_func

result = con_func('Hello', 'Liubomyr!')
print(result)

def function_a (*args, **kwargs):
    result = 1
    for number in args:
        result *= number

    print(result)

function_a(4, 3, 6, 2, c = 5)


numbers = (1, 2, 3, 4, 5)

result = 1

for number in numbers:
    result *= number

print(result)


user_info1 = {"username": "student-one", "password": "demo-password", "age": 24, "Hobbies": ["Swimming", "Diving"]}
user_info2 = {
    "username": "student-two",
    "password": "demo-password",
    "age": 27,
    "Hobbies": {
        "main-hobbies": "Soccer",
        "Other_hobbies": [
            "Skiing",
            "Volleyball"
        ]
    }
}

users = [user_info1, user_info2]

print(users[0]["age"])

for user in users:
    print(user["Hobbies"]["Other_hobbies"][0])
    print(user.get("Hobbies", "Error: User(s) Info Not Found!"))

print(isinstance(user_info1, dict))


products = ["apples", "bananas", "pineapples"]
prices = [50, 40, 90]

# print(list(zip(products, prices)))

for goods in zip(products, prices):
    print(goods)


numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number ** 2)

print(result)


result = map(lambda number: number ** 2, numbers)
print(list(result))
print(sum(numbers))
