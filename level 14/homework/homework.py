#for loop
#for loop HOMEWORK   N1
for i in range(21):
    print(i)
#Print the first 10 natural numbers.  N2
for i in range(1, 11):
    print(i)
# 0 to 100    N3
print("Even numbers from 0 to 100:")
for i in range(0, 101, 2):
    print(i)
#odd number  N3 
print("\nOdd numbers from 0 to 100:")
for i in range(1, 101, 2):
    print(i)


#while loop
#N1
num = 20
while num <= 2:
    print(num)
    num += 2
#N3
ans = int(input("enter number from 0 to 10:"))
while ans != 7:
    ans = int(input("enter number from 0 to 10:"))
    if ans == 7:
        print("that is correct")

#N4
numbers = [1, 2, 3, 4, 5]

index = 0
new_numbers = []

while index < len(numbers):
    doubled_number = numbers[index] * 2
    new_numbers.append(doubled_number)
    index += 1

print( numbers)
print( new_numbers)

#N5
correct_password = "password123"

password = input("Enter the password: ")

while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")

print("Login successful!")

#if - else
#N1
import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

#2
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#3
temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

#4
score = float(input("Enter your exam score: "))

if score >= 50:
    print("You passed!")
else:
    print("You failed.")

#5
age = int(input("Enter your age: "))

if 13 <= age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")

#for loop
#N1
for num in range(1, 51):
  
    if num > 1:
        
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
#N2
for num in range(1, 16):
    square = num ** 2
    print(f"The square of {num} is: {square}")

#N3 
num = int(input("Enter number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)

#N4
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)

#5
number = int(input("Enter a number to generate its multiplication table: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11): 
    print(f"{number} x {i} = {number * i}")

#WHILE LOOP 
#1
a, b = 0, 1
count = 0

while count < 50:
    print(a, end=' ')
   
    a, b = b, a + b
    count += 1
#N3
def sum_of_digits(number):
 
    sum_digits = 0

    while number > 0:
        
        digit = number % 10
        
        sum_digits += digit
      
        number //= 10
    
    return sum_digits

num = int(input("Enter a number to calculate the sum of its digits: "))

result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}.")

#N4

def reverse_list(nums):
   
    reversed_list = []
 
    index = len(nums) - 1
    
    while index >= 0:
        reversed_list.append(nums[index])
        index -= 1
    
    return reversed_list

numbers = input("Enter numbers separated by spaces: ").split()

numbers = list(map(int, numbers))

reversed_numbers = reverse_list(numbers)

print("Reversed list:", reversed_numbers)

#N5

#IF ELSE
#N1
year = int(input("Enter a year to check if it's a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#N3
number = float(input("Enter a number to determine if it's positive, negative, or zero: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")

#N5
year = int(input("Enter a year to check if it's a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
