
def sum_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers_list)
print("Sum of even numbers:", result)

#
def reverse_string(input_string):
    reversed_str = ""   
    for i in range(len(input_string) - 1, -1, -1):
        reversed_str += input_string[i]   
    return reversed_str
input_str = "how are you"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)

#
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"The factorial of {num} is:", result)

#
def count_vowels(s):
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0 
    for char in s:
        if char in vowels:
            vowel_count += 1    
    return vowel_count
input_str = "Goa is the best"
result = count_vowels(input_str)
print("Number of vowels in the string:", result)

#
def is_prime(num):

    if num <= 1:
        return False
    
    for i in range(2, int(num**2) + 1):
        if num % i == 0:
            return False   
    return True
print(is_prime(5))   
print(is_prime(19))  
print(is_prime(25))  
print(is_prime(10))   
print(is_prime(0))

#

