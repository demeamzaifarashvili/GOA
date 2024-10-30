a = 5
b = 10

sum_result = a + b

print(":", sum_result)



str1 = "hello"
str2 = "world"

both_str = str1 + " " + str2

print("", both_str)


print(5 == 5)  # True

print(5 != 4)  # True

print(9 > 6)   # True

print(7 >= 7)  # True

print(2 < 5)   # True

print(5 <= 5)  # True


a = 16
b = 5
result = (a + b) > 10
print(result) 

a = 19
b = 3
is_less = (a < b)
print(is_less) 


#True and True = True
#True and False = False
#False and True = False
#False and False = False

#True or True = True
#True or False = True
#False or True = True
#False or False = False

#not True = False
#not False = True

print(True and True)   # True
print(True and False)  # False

print(True or False)   # True
print(False or False)  # False

print(not True)        # False
print(not False) 



for i in range(1, 11):
    print(i)


i = 1

while i <= 10:
    print(i)
    i += 1 


text = "Hello, World!"

for reach in text:
    print(reach)


def calculat(numbers):
    if len(numbers) == 0:
        return 0  

    total = sum(numbers)  
    average = total / len(numbers) 
    return average

test_case = [1, 3, 4, 5, 2]
average_result = calculat(test_case)
print(f"sash: {average_result}")


i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue 
    print(i) 
    i += 1 


total = 0
number = 1

while total < 50:
    total += number  
    number += 1