
#codwars 8kyu

#1) https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
#2) https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
#3) https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
#4) https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
#5) https://www.codewars.com/kata/523b4ff7adca849afe000035/train/python


def manual_sum(numbers):
    total = 0 
    for number in numbers:  
        total += number 
    return total  

example_list = [ 5, 6, 7 , 1, 2, 3, 4, 5]
result = manual_sum(example_list)
print(f"total: {result}")


def manual_len(seq):
    count = 0  
    for item in seq:  
        count += 1  
    return count  

string = "Hello, deme"
result_length = manual_len(string)
print(f"len: {result_length}")