#1
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



#2
numbers = [1,2,3,4,5,6,7,8]
numbers_copy = numbers
numbers_copy[0] = "demetre"
print(numbers_copy)
print(numbers)


#3
def even_list(number_list):
    res_list = []

    for num in number_list:
        if num%2 == 0:
            res_list.append(num)
        return res_list
    print(even_list([1,2,3,4,5,6,7,8,9]))  


#4
name = "dEMeTRE"  
print(name.upper())


#5
user_name = "DEMETRE"  #patara asoebit wers
print(user_name.lower())
