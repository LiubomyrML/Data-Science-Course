import json
import os

with open("database.json", "r") as f:
    result = json.load(f)
    print(result[0]["user"])

demo_user = {
    "user": "student",
    "password": "demo-password",
}
result.append(demo_user)

with open("database.json", "w") as f:
    json.dump(result, f, indent=4)


import pickle

with open("database_b_.pkl", "wb") as f:
    pickle.dump(demo_user, f)

with open("database_b_.pkl", "rb") as f:
    print(pickle.load(f))


try:
    with open("database_b_.pkl", "rb") as f:
        data = pickle.load(f)
except TypeError:
    print("Error!!!")
else:
    print(data)


from collections import defaultdict

count_cars = defaultdict(lambda: 0)
count_cars["green"] += 1
count_cars["yellow"]
print(dict(count_cars))


from collections import Counter

sentence = "I Love Python!"
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
print(dict(Counter(sentence))["o"])
print(dict(Counter(numbers)))


from itertools import product

team_a = ["Alex", "Mike", "John"]
team_b = ["Anna", "Yaroslav", "Denis"]
team_c = ["Irina", "Olena", "Arthur"]

print(*product(team_a, team_b, team_c))


from itertools import permutations

goods = ("Bananas", "Apples", "Pears", "Chocolates Bars")

print(*permutations(goods))


from itertools import combinations

players = ['Alex', 'Mike', 'John', 'Anna', 'Yaroslav', 'Denis', 'Irina', 'Olena', 'Arthur']
print(*combinations(players, 3))


import requests

city = input("Type your City:")
api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

if not api_key:
    print("Set OPENWEATHERMAP_API_KEY to check the weather.")
else:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key},
        timeout=10,
    )

    if response.status_code == 200:
        print(response.json()["weather"])
    else:
        print(response.json()["message"])
