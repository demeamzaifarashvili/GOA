def say_hello():
    return "Hello, world!"

print(say_hello())


def greet(name):
    return f"Hello, {name}!"


print(greet("deme"))

def multi(a, b):
    return a * b

print(multi(3, 2)) 


def sum(a, b, c):
    return a + b + c

print(sum(3, 4, 8))


def is_adult(age):
    return "adult" if age >= 18 else "not adult"

print(is_adult(19))  
print(is_adult(15))
