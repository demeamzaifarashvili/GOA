#CODEWARS
#1
score = float(input("please enter number (0-100): "))

if 90 <= score <= 100:
    grade = "Grade A"
elif 80 <= score < 90:
    grade = "Grade B"
elif 70 <= score < 80:
    grade = "Grade C"
elif 60 <= score < 70:
    grade = "Grade D"
elif 0 <= score < 60:
    grade = "Grade F"
else:
    grade = "wrong"

print(grade)

#2
sum1 = 0
number = 1

while sum < 50:
    sum += number
    number += 1

print("{sum1},  {number - 1}")

#3
while number <= 100:
    if 50 <= number < 60:
        number += 1 
    print(number)
    number += 1


#4
def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a
    
#5
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]


#6
a = "code"
b = "wa.rs"
name = a + b


#7
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]



