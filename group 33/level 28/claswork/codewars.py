#1
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

#2
def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count