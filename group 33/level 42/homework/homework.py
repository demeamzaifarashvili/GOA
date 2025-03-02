#1
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        years += 1
    return years

#2
def open_or_senior(data):
    result = []
    for person in data:
        age, handicap = person
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

#3
def row_sum_odd_numbers(n):
    return n ** 2

#4,5?
