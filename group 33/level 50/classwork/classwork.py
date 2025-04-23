#codewars

#1
def filter_list(l):
    return [item for item in l if isinstance(item, int)]

#2
def solve(s):
    lower = sum(1 for c in s if c.islower())
    upper = sum(1 for c in s if c.isupper())
    return s.lower() if lower >= upper else s.upper()

#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#4
def reverse_list(l):
    return l[::-1]






#6 kyu
#5 
def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]

        
#6
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
  
    array1_squared = [i ** 2 for i in array1]

    return sorted(array1_squared) == sorted(array2)
