numbers = [i for i in range(1, 101)]
print(numbers)


print("_______________________")


numbers2 = [i for i in range(1, 101) if i % 2 == 0]
print(numbers2)


print("_______________________")


squares = [i**2 for i in range(1, 11)]
print(squares)


print("_______________________")


names = ["deme", "nika", "gio", "luka", "mate"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)