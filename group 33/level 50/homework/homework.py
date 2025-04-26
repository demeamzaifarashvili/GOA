#1
def solve(s):
    count_u = 0
    count_l = 0
    
    for char in s:
        if char.isupper():
            count_u += 1
        else:
            count_l += 1
    
    if count_u <= count_l:
        return s.lower()
    else:
        return s.upper()
    
#2
def greet(username = "guest"):
    print("hello deme")
greet()

def add(num1, num2, operation):
    if operation == "+":
        print(num1 + num2)
add(5, 7,"+")


#3
def sum_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers_list)
print("Sum of even numbers:", result)


#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"The factorial of {num} is:", result)
