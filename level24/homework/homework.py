def proc_numbers(int_list):
    result_list = []
    
    for num in int_list:
        if num % 2 == 0:

            result_list.append(num * num)
        else:

            result_list.append(num + 2)

    return result_list

numbers = [1, 2, 3, 4, 5]
print(proc_numbers(numbers))


def find_longest_word(word_list):
    if not word_list:
        return None 
    
    longest_word = word_list[0] 
   
    for word in word_list[1:]:
        if len(word) > len(longest_word):
            longest_word = word  
    
    return longest_word

words = ["apple", "banana", "cherry", "date"]
print(find_longest_word(words))