#extend
numbers1 = [1,2,4,5,7,8,]
numbers2 = [4,6,7,8,0,1,]
numbers1.extend(numbers2)
print(numbers1)
#
numbers4 = [1,2,4,5,7,8,]
numbers3 = ["luka", "deme", "dachi"]
numbers4.extend(numbers3)
print(numbers4)
#
numbers4 = ["nia", "maka"]
numbers5 = ["deme", "oto",]
numbers4.extend(numbers5)
print(numbers4)
#
numbers6 = [6,7,"deme"]
numbers7 = [4,5,"nino"]
numbers6.extend(numbers7)
print(numbers6)
#
numbers6 = [6,7,True]
numbers7 = [4,5,False]
numbers6.extend(numbers7)
print(numbers6)
#insert
names = ["luka", "deme", "nika"]
names.insert(2,  "lola")
print(names)
#
name = ["luka", "deme", "nika"]
name.insert(2,  4)
print(name)
#
name1 = ["luka", "deme", "nika"]
name1.insert(3,  True)
print(name1)
#
name2 = ["luka", "deme", "nika"]
name2.insert(1,  "deme")
print(name2)
#
name3 = ["luka", "deme", "nika"]
name3.insert(3,  45)
print(name3)
#clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
#
cars = ["bmw","mercedes"]
cars.clear()
print(cars)
#
cars1 = ["bmw",4]
cars1.clear()
print(cars1)
#
cars2 = ["bmw",True]
cars2.clear()
print(cars2)
#
cars3 = [4,5,6,8,9,0,9,8]
cars3.clear()
print(cars3)
#copy
numbers = [1,2,3,4,5,6,7,8]
numbers_copy = numbers
numbers_copy[0] = "demetre"
print(numbers_copy)
print(numbers)
#
numbers1 = [1,2,3,4,5,6,7,8]
numbers_copy = numbers1
numbers_copy[0] = True
print(numbers_copy)
print(numbers1)
#
nam = ["demetre","giorgi"]
nam_copy = nam
nam_copy[0] = "nika"
print(nam_copy)
print(nam)
#
age = [25,26,29]
age_copy = age
age_copy [1] = 30
print(age_copy)
print(age)
#
list9 = [True,True,False]
list9_copy = list9
list9_copy [0] = False
print(list9_copy)
print(list9)
#pop
list = [1, 2, 3, 4, 5]
list.pop(2)
print (list)
#
list1 = ["deme","nika"]
list1.pop(1)
print (list1)
#
list2 = ["deme","nika"]
list2.pop(0)
print (list2)
#
list3 = ["deme","nika","gio","dato"]
list3.pop(3)
print (list3)
#
list4 = ["deme","nika","oto","rati"]
list4.pop(2)
print (list4)
#appand
cars = ["bmw","mercedes","lambo"]
cars.append("pagani")
print(cars)
#
cars1 = ["bmw","mercedes","audi"]
cars1.append(4)
print(cars1)
#
number8 = [1,3,4,5,7,8]
number8.append(True)
print(number8)
#
number9 = [1,3,4,9,2,1,5]
number9.append("Demetre")
print(number9)
#
number7 = [1,3,4,]
number7.append("deme")
print(number7)
#count
letter = ["b","b","b","e"]
print(letter.count("b"))
#
name = ["nato","deme","nato"]
print(name.count("nato"))
#
cars9 = ["opel","nissan","fit"]
print(cars9.count("opel"))
#
my_list = [True,"deme",3,3]
print(my_list.count(3))
#
my_list5 = [True,"deme",3,3]
print(my_list5.count("nika"))
#
numbers1 = ["deme","nika","luka"]
numbers2 = [3,4,5,6,8,9,9]
numbers1.extend(numbers2)
print(numbers1)
#
def separate_lists(lst):
    integers = []
    strings = []

    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
           
    return integers, strings

mixed_list = [1, 'hello', 3, 'world', 5, 'python', 7]
integers, strings = separate_lists(mixed_list)

print("Integers:", integers)
print("Strings:", strings)
#
def separate_odd_even_and_sum(list1, list2):
    odd_sum = 0
    even_sum = 0
    

    def is_odd(num):
        return num % 2 != 0

    for num in list1:
        if is_odd(num):
            odd_sum += num
        else:
            even_sum += num

    for num in list2:
        if is_odd(num):
            odd_sum += num
        else:
            even_sum += num
    
    return odd_sum, even_sum

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

odd_sum, even_sum = separate_odd_even_and_sum(list1, list2)

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")



