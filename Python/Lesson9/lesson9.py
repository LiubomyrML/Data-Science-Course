# 1
def get_even_numbers():
    return list(filter(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5]
print(get_even_numbers())


# 2
spysok = ["abcde", "def", "rtinbkkio"]
def filter_spysok(x, y):
    result =[]
    for n in x:
        if len(n)>y:
            result.append(n)
    return result
print(filter_spysok(spysok, 5))


# 3
def lower_sentence(sentence):
    return sentence.lower()
sentence = "I LOVE PYTHON!"
sentence_lower = "".join(map(lower_sentence, sentence))
print(sentence_lower)


# 4
arr = [1, 2, 3, 4, 5]

def square_root(numbers: list):
    return list(map(lambda number: number ** 2, numbers))

print(square_root(arr))


# 5
def squared_sum_of_odd_nums(numbers: list):
     odd_numbers = []
     for number in numbers:
         if number % 2 != 0:
             odd_numbers.append(number ** 2)
     return sum(odd_numbers)

print(squared_sum_of_odd_nums([1, 2, 3, 4, 5]))


# DateTime

from datetime import datetime, timedelta

print(datetime.now())
print(datetime.now() + timedelta(days=7, hours=2))
print(datetime(year=2026, month=10, day=1) + timedelta(days=7))
print(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
print(datetime.strptime("2026-10-15", "%Y-%m-%d") + timedelta(days=7))


# start_time = datetime.now()
#
# for i in range(10000000):
#     print(i)
#
# result = datetime.now() - start_time
#
# print(result.seconds)


# 6
from datetime import datetime

class Car:
    def __init__(self, mark: str, model: str, year: int):
        self.mark = mark
        self.model = model
        self.year = year

    def get_year(self):
        now  = datetime.now()
        return now.year - self.year

car = Car("Volvo", "xc90", 2020 )
print(car.get_year())