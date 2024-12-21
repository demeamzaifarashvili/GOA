numbers = [2, 7, 9, 8, 10]
numbers2 = list(map(lambda x: x * 2, numbers))
print(numbers2)

str = ["apple", "bmw", "lemon"]
lengths = list(map(len, str))
print(lengths)

numbers2 = [10, 55, 42, 78, 65, 20]
num50 = list(filter(lambda x: x > 50, numbers2))
print(num50)