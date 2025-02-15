#1
def odd_count(n):
    return n // 2

#2
def find_difference(a, b):
    volume_a = a[0] * a[1] * a[2]
    volume_b = b[0] * b[1] * b[2]
    return abs(volume_a - volume_b)

#3
def two_sort(array):
    sorted_array = sorted(array)
    
    first_string = sorted_array[0]
    result = '***'.join(first_string)
    
    return result

#4
def reverse_list(l):
    return l[::-1]

#5
def is_palindrome(s):
    normalized_s = s.lower()
    return normalized_s == normalized_s[::-1]