#1
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

#2
def friend(x):
    return [name for name in x if len(name)==4]

#3
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]

#4
def longest(a1, a2):
 return ''.join(sorted())

#5
def get_sum(a, b):
    
    start = min(a, b)
    end = max(a, b)
    
    return sum(range(start, end + 1))
    