import random

class RandomNumberIterator:
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.count:
            self.current_count += 1
            return random.randint(self.start, self.end)
        raise StopIteration

iterator = RandomNumberIterator(5, 1, 10)
print('task 1.1:')
for number in iterator:
    print(number)

#############################################

def random_numbers(count, start, end):
    for _ in range(count):
        yield random.randint(start, end)

print('task 1.2:')
for number in random_numbers(5, 1, 10):
    print(number)

############################################

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def add_ten(numbers):
    for number in numbers:
        yield number + 10

fibonacci_generator = fibonacci()
fibonacci_numbers = [next(fibonacci_generator) for _ in range(5)]

fibonacci_with_ten = add_ten(fibonacci_numbers)
print('task 1.3:')
for number in fibonacci_with_ten:
    print(number)

############################################

data = {
    'Russia': ['Moscow', 'Saint Petersburg', 'Novosibirsk'],
    'USA': ['New York', 'Los Angeles', 'Chicago'],
    'France': ['Paris', 'Marseille', 'Lyon']
}

cities = ['Moscow', 'Paris', 'Chicago']

def find_country(city):
    for country, city_list in data.items():
        if city in city_list:
            return country
    return 'Unknown'
print('task 1.4:')
for city in cities:
    country = find_country(city)
    print(f"The city {city} is located in {country}")