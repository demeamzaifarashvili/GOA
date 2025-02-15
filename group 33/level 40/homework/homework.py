#1
def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a
    
#2
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]

#3
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]

#4
a = "code"
b = "wa.rs"
name = a + b