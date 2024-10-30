number = 1

while number <= 100:
    if 50 <= number < 60:
        number += 1 
    print(number)
    number += 1

sum1 = 0
number = 1

while sum < 50:
    sum += number
    number += 1

print("{sum1},  {number - 1}")



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