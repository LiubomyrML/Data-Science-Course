def sum(a, b):
    return a + b

print(sum(10, 20))


numbers = [1, 2, 3, 4, 5]

def sum_list(numbers_list):
    result = 0
    for number in numbers_list:
        result += number
    print(result)

sum_list(numbers)


def greeting(greeting_word: str, name: str = 'Unknown'):
     print(f'{greeting_word} {name}!')

greeting('Hello', 'Roman')
greeting('Hello')


numbers = [21, 435, 9, 15]
sorted_numbers = sorted(numbers, key=lambda number: number, reverse=True)

print(sorted_numbers)