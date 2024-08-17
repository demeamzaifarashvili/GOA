# 1 Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
# 2 Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
numbers = [1, 2, 3]
print(square_sum(numbers))

# 3  Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time since midnight in milliseconds

def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000

# 4  Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

def dna_to_rna(dna):
    return dna.replace('T', 'U')

# 5  Write a function which takes a number and returns the corresponding ASCII char for that value.

def get_char(c):
   return chr(c)