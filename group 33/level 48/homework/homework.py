#1
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
#2
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
numbers = [1, 2, 3]
print(square_sum(numbers))

#3
def positive_sum(arr):
    sum=0
    for i in arr:
        if i > 0:
            sum += i
        return sum
    
#4
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
    
#5
def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        
#6
cars1 = ["bmw",4]
cars1.clear()
print(cars1)

#7
numbers1 = [1,2,4,5,7,8,]
numbers2 = [4,6,7,8,0,1,]
numbers1.extend(numbers2)
print(numbers1)

#8
cars = ["bmw","mercedes","lambo"]
cars.append("pagani")
print(cars)